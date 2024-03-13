from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from api.authentication import Authentication
from api.models import Vehicle, VehicleType
from api.serializers import VehicleSerializer, VehicleTypeSerializer, UserSerializer


class Login(ObtainAuthToken):
    """
    Inicio de sesión (rest_framework AuthToken)

    <server>:<host>/login/?username=<username>&password=<password>

    :param username: Nombre de usuario
    :param password: Contraseña de usuario

    :return: token, user({username, email, first_name, last_name}), message
    """

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        if login_serializer.is_valid():
            print(login_serializer.is_valid())
            user = login_serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            user_serializer = UserSerializer(user)
            if not created:
                token.delete()
                token = Token.objects.create(user=user)

            return Response({
                'token': token.key,
                'user': user_serializer.data,
                'message': 'Inicio de sesión exitoso'
            }, status=status.HTTP_201_CREATED)

        else:
            print("No pasó la validación")
            return Response({'mensaje': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)


class Logout(APIView):
    """
    Cierre de sesión (rest_framework AuthToken)
    <server>:<host>/logout/?token=<token>

    :param token: Token válido del usuario

    :return: token_message
    """

    def post(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        if token:
            token = Token.objects.filter(key=token).first()
            if token:
                token.delete()
                return Response({
                    'token_message': 'Token eliminado'
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'error': 'Credenciales inválidas'
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'error': 'No se ha encontrado el token en la petición'
            }, status=status.HTTP_409_CONFLICT)


class UserViewSet(Authentication, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VehicleViewSet(Authentication, viewsets.ModelViewSet):
    """
    API de Vehículos

    :param Marca:str
    :param Modelo:str
    :param Color:str
    :param Patente:str
    :param Aseguradora:str
    :param Expiración de Poliza:str
    :param Tipo de vehículo:ID del tipo de vehículo (VehicleType)
    """

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleTypeViewSet(Authentication, viewsets.ModelViewSet):
    """
    API de tipos de vehículos

    param: Nombre:str
    """

    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
