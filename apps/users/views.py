from datetime import datetime
from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from apps.users.api.serializers import UserTokenSerializer

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
                        #Borrar sesion si ya es que exista una activa del usuario
                    #Obtengo todas las sesiones que su tiempo de expiracion sea mayor o igual a la hora actual
                    sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    print(sessions)
                    if sessions.exists():
                        for session in sessions:
                            print(session)
                            #Se decodifica la sesion
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get("_auth_user_id")):
                                print("Se elimina la sesion")
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
