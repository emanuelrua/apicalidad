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
