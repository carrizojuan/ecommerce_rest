from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.api.serializers import UserSerializer, TestUserSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from apps.users.models import User

""" class UserApiView(APIView):

    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data) """

@api_view(["GET","POST"])
def user_api_view(request):
    if request.method == "GET":

        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)

        test_data = {
            "name": "juancho",
            "email":"pepe@pepe.com"
        }

        test_user = TestUserSerializer(data = test_data, context=test_data)

        if test_user.is_valid():
            print("Es valido el test user")
        else:
            print(test_user.errors)

        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def user_detail_view(request, pk=None):

    user = User.objects.filter(id = pk).first()

    if user:

        if request.method == "GET":
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == "PUT":
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            user = User.objects.filter(id = pk).first()
            user.delete()
            return Response({"message": f"Usuario {str(pk)} eliminado correctamente"}, status=status.HTTP_200_OK)
    
    else:

        return Response({"message": f"No se ha encontrado un usuario con estos datos"} ,status=status.HTTP_400_BAD_REQUEST)