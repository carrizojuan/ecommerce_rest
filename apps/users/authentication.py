from ecommerce_rest.settings.base import TOKEN_EXPIRED_AFTER_SECONDS
from rest_framework.authentication import TokenAuthentication
from django.utils import timezone
from datetime import timedelta

class ExpiringTokenAuthentication(TokenAuthentication):

    expired = False

    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expire_handler(self,token):
        is_expired = self.is_token_expired(token)
        #Aca hacer toda la logica
        if is_expired:
            self.expired = True
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user = user)

        return is_expired,token

    def authenticate_credentials(self, key):
        model = self.get_model()
        token, message = None, None
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            message = "Token invalido"
            self.expired = True
            
        if token is not None:
            if not token.user.is_active:
                message = "Usuario inactivo o eliminado"

            is_expired, token = self.token_expire_handler(token)

            if is_expired:
                message = "Su token ha expirado"
                

        return (token, message, self.expired)