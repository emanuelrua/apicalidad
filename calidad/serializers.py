from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class AsesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asesor
        fields = '__all__'
        read_only_field = ('FechaRegistro', 'Documento',)

    def validate_Documento(self, value):
        # Verifica si ya existe un asesor con el mismo número de documento
        if Asesor.objects.filter(Documento=value).exists():
            raise serializers.ValidationError(
                'Ya existe un asesor con este número de documento.')
        return value


class CapacitadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capacitador
        fields = '__all__'


class EvaluacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluaciones
        fields = '__all__'


class JornadaSerializers (serializers.ModelSerializer):
    class Meta:
        model = Jornada
        fields = '__all__'


class SexoSerializers (serializers.ModelSerializer):
    class Meta:
        model = Sexo
        fields = '__all__'


class ZonalSerializers (serializers.ModelSerializer):
    class Meta:
        model = Zonal
        fields = '__all__'

class TipoTrabajoSerializers (serializers.ModelSerializer):
    class Meta:
        model = TipoTrabajo
        fields = '__all__'

class HorarioSerializers (serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

class EstadoSerializers (serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class CargoSerializers (serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')  # Se extrae la contraseña
        user = User(**validated_data)
        user.set_password(password)  # Se encripta la contraseña
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs