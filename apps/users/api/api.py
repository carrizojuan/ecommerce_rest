from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.api.serializers import UserSerializer
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

        #Le paso al serializador la lista de todos los usuarios y lo convierte en json, many=true porque son varios
        users_serializer = UserSerializer(users, many=True)

        #Retorno la respuesta pasandole los datos de la instancia del serializador junto al status 200
        return Response(users_serializer.data, status=status.HTTP_200_OK)
        """ test_data = {
            "name": "juancarlos",
            "email":"pepe@pepe.com"
        }

        test_user = TestUserSerializer(data = test_data, context=test_data)

        if test_user.is_valid():
            user_validate = test_user.save()
            print(user_validate)
        else:
            print(test_user.errors) """

        
    
    elif request.method == "POST":

        #Le paso al serializador los datos que vienen del request para que lo convierta de json a una instancia de usuario
        user_serializer = UserSerializer(data=request.data)

        #Pregunto si son validos los datos que llegaron del request
        if user_serializer.is_valid():

            #Con el metodo save del serializador llama a un metodo create interno que lo que hace es crear al usuario con los datos validados anteriormente
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        
        #Si hay un error en la validacion retorno el mensaje de error que arroja el serializador
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def user_detail_view(request, pk=None):

    #Obtengo al usuario utilizando el pk que llega de la url
    user = User.objects.filter(id = pk).first()

    if user:

        if request.method == "GET":
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == "PUT":

            """ user_serializer = TestUserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save() """
                
            #Le paso al serializador el usuario a actualizar y los datos nuevos
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

        #Si no encuentra un usuario con ese pk arroja una respuesta y un codigo de Bad Request
        return Response({"message": f"No se ha encontrado un usuario con estos datos"} ,status=status.HTTP_400_BAD_REQUEST)