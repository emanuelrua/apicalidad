from django.shortcuts import render
from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class AsesorViewSet(viewsets.ModelViewSet):
    queryset = Asesor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AsesorSerializer


class CapacitadorViewSet(viewsets.ModelViewSet):
    queryset = Capacitador.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CapacitadorSerializer

class EvaluacionesViewSet(viewsets.ModelViewSet):
    queryset = Evaluaciones.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EvaluacionesSerializer

class JornadaViewSet(viewsets.ModelViewSet):
    queryset = Jornada.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = JornadaSerializers

class SexoViewSet(viewsets.ModelViewSet):
    queryset = Sexo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SexoSerializers

class ZonalViewSet(viewsets.ModelViewSet):
    queryset = Zonal.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ZonalSerializers

class TipoTrabajoViewSet(viewsets.ModelViewSet):
    queryset = TipoTrabajo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoTrabajoSerializers

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = HorarioSerializers

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EstadoSerializers

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CargoSerializers


