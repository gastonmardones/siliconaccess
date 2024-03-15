from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from api.authentication import Authentication
from api.models import Vehicle, VehicleType, VehicleRecord
from api.serializers import VehicleSerializer, VehicleTypeSerializer, UserSerializer, VehicleRecordSerializer


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

    :param brand:str
    :param model:str
    :param color:str
    :param license:str
    :param insurance:str
    :param insurance_expiration:date
    :param type:VehicleType
    """

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleTypeViewSet(Authentication, viewsets.ModelViewSet):
    """
    API de tipos de vehículos

    :param name:str
    """

    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class VehicleRecordViewSet(Authentication, viewsets.ModelViewSet):
    """
    API de Ingreso y Egreso de Vehículos

    :param vehicle:Vehicle
    :param entry_datetime:(auto_created)
    :param exit_datetime:datetime
    """
    queryset = VehicleRecord.objects.all()
    serializer_class = VehicleRecordSerializer
