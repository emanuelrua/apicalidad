from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework import permissions
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework import views
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


@api_view(['GET', 'POST'])
@login_required
def asesor(request):
    if request.method == 'GET':
        asesor = Asesor.objects.all()
        serializer = AsesorSerializer(asesor, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AsesorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
@login_required
def asesordni(request, Documento):
    if request.method == 'GET':
        asesor = Asesor.objects.get(Documento=Documento)
        serializer = AsesorSerializer(asesor)
        return Response(serializer.data)


@api_view(['PUT', 'PATCH'])
@login_required
def asesor_update(request, pk):
    try:
        asesor = Asesor.objects.get(pk=pk)
    except Asesor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AsesorSerializer(asesor, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@login_required
def capacitador(request):
    if request.method == 'GET':
        capacitador = Capacitador.objects.all()
        serializer = CapacitadorSerializer(capacitador, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CapacitadorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['PUT', 'PATCH'])
@login_required
def capacitador_update(request, pk):
    try:
        capacitador = Capacitador.objects.get(pk=pk)
    except Capacitador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CapacitadorSerializer(
        capacitador, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@login_required
def evaluaciones(request):
    if request.method == 'GET':
        evaluaciones = Evaluaciones.objects.all()
        serializer = EvaluacionesSerializer(evaluaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EvaluacionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
@login_required
def evaluacionesasesor(request, asesor_id):
    if request.method == 'GET':
        evaluaciones = Evaluaciones.objects.filter(Asesor_id=asesor_id)
        serializer = EvaluacionesSerializer(evaluaciones, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@login_required
def jornada(request):
    if request.method == 'GET':
        jornada = Jornada.objects.all()
        serializer = JornadaSerializers(jornada, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = JornadaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
@login_required
def sexo(request):
    if request.method == 'GET':
        sexo = Sexo.objects.all()
        serializer = SexoSerializers(sexo, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SexoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
@login_required
def zonal(request):
    if request.method == 'GET':
        zonal = Zonal.objects.all()
        serializer = ZonalSerializers(zonal, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ZonalSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
@login_required
def tipotrabajo(request):
    if request.method == 'GET':
        tipotrabajo = TipoTrabajo.objects.all()
        serializer = TipoTrabajoSerializers(tipotrabajo, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TipoTrabajoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
@login_required
def horario(request):
    if request.method == 'GET':
        horario = Horario.objects.all()
        serializer = HorarioSerializers(horario, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HorarioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
@login_required
def estado(request):
    if request.method == 'GET':
        estado = Estado.objects.all()
        serializer = EstadoSerializers(estado, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EstadoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
@login_required
def cargo(request):
    if request.method == 'GET':
        cargo = Cargo.objects.all()
        serializer = CargoSerializers(cargo, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CargoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer


# home page
def home(request):
    return render(request, 'index.html')

# create user


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm,
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('homeapi')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'})
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Contraseñas no coinciden'})

# home page


def homeapi(request):
    return render(request, 'indexapi.html')

# logout


def signout(request):
    logout(request)
    return redirect('home')

# login


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm,
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña incorrectos'})
        else:
            login(request,user)
            return redirect('homeapi')