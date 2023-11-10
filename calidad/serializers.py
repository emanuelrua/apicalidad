from rest_framework import serializers
from .models import *


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
