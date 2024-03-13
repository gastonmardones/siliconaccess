from django.conf import settings
from django.utils import timezone
from rest_framework import status, exceptions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import get_authorization_header
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class Authentication(object):
    """
    Agrega autenticación personalizada para las views que hereden de esta clase.
    """

    def dispatch(self, request, *args, **kwargs):
        try:
            ExpiringTokenAuthentication().authenticate(request)
            return super().dispatch(request, *args, **kwargs)

        except Exception as err:
            response = Response({'error': err.detail}, status=status.HTTP_400_BAD_REQUEST)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = 'aplication/json'
            response.renderer_context = {}
            return response


class ExpiringTokenAuthentication(TokenAuthentication):
    """
    Autenticación basada en token personalizada.

    El cliente deberia autenticarse pasando el token en el header.
    Ejemplo:
    Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a

    """

    @staticmethod
    def is_expired(token):
        """
        Chequea que si el token ya expiró
        basándose en los segundos definidos en la setting TOKEN_EXPIRE_SECONDS
        y la creación del token.
        """

        expire_time = token.created + timezone.timedelta(seconds=settings.TOKEN_EXPIRE_SECONDS)
        return timezone.now() > expire_time

    def authenticate(self, request):
        """
        Verifica que exista el token y sea válido.
        """
        try:
            token = get_authorization_header(request).split()[1].decode()
        except:
            raise exceptions.AuthenticationFailed('No se han enviado las credenciales.')

        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=token)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Token inválido.')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('Usuario inactivo o eliminado.')
        elif self.is_expired(token):
            raise exceptions.AuthenticationFailed('Token expirado.')
