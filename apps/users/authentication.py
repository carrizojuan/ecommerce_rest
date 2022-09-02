from ecommerce_rest.settings.base import TOKEN_EXPIRED_AFTER_SECONDS
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils import timezone
from datetime import timedelta

class ExpiringTokenAuthentication(TokenAuthentication):

    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expire_handler(self,token):
        is_expired = self.is_token_expired(token)
        return is_expired

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise AuthenticationFailed('Token invalido')

        if not token.user.is_active:
            raise AuthenticationFailed('Usuario inactivo o eliminado')
        
        is_expired = self.token_expire_handler(token)
        if is_expired:
            print("Token expirado")
            raise AuthenticationFailed("Su token ha expirado")

        return (token.user, token)