from datetime import datetime
from msilib.schema import Error
from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from apps.users.api.serializers import UserTokenSerializer
from apps.users.models import User

class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data["user"]
            if user.is_active:
                token, created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response(
                        {
                            "user": user_serializer.data,
                            "token": token.key,
                            "message": "Inicio de Sesion exitoso"
                        },
                        status=status.HTTP_201_CREATED
                    )
                else:
                        #Borrar sesion si ya es que exista una sesion activa del usuario
                    #Obtengo todas las sesiones que su tiempo de expiracion sea mayor o igual a la hora actual
                    sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if sessions.exists():
                        for session in sessions:
                            #Se decodifica la sesion
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get("_auth_user_id")):
                                session.delete() 
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response(
                        {
                            "user": user_serializer.data,
                            "token": token.key,
                            "message": "Inicio de Sesion exitoso"
                        },
                        status=status.HTTP_202_ACCEPTED
                    )
            else:
                return Response({"message": "Usuario no activo"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({'message': 'Error en autenticacion'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    
    def post(self, request, *arg, **kwargs):

        try:
            username = request.POST["username"]
            user = User.objects.get(username = username)
            token = Token.objects.filter(user = user).first()
            if token:
                user = token.user
                sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if sessions.exists():
                    for session in sessions:
                        #Se decodifica la sesion
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get("_auth_user_id")):
                            session.delete() 
                token.delete()

                session_message = "Sesion eliminada correctamente"
                token_message = "Token eliminado correctamente"

                return Response({"session_message": session_message, "token_message": token_message},
                                status = status.HTTP_200_OK) 
            return Response({"error_message": "No se ha encontrado un usuario logueado con estas credenciales"},
                            status = status.HTTP_400_BAD_REQUEST)
        except ValueError: 
            
            print(ValueError)
            return Response({"error_message": "No se ha encontrado un token asociado al usuario"}, 
                            status = status.HTTP_409_CONFLICT)
