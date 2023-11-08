from django.db import models
from django.utils import timezone


class Jornada(models.Model):
    Descripcion = models.CharField(max_length=50)


class Sexo(models.Model):
    Descripcion = models.CharField(max_length=10)


class Zonal(models.Model):
    Descripcion = models.CharField(max_length=50)


class TipoTrabajo(models.Model):
    Descripcion = models.CharField(max_length=50)


class Horario(models.Model):
    Descripcion = models.CharField(max_length=50)


class Cargo(models.Model):
    Descripcion = models.CharField(max_length=20)


class Estado(models.Model):
    Descripcion = models.CharField(max_length=20)


class Capacitador(models.Model):
    Nombres = models.CharField(max_length=50)
    ApellidoPaterno = models.CharField(max_length=50)
    ApellidoMaterno = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=20)
    Correo = models.CharField(max_length=100)
    Cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)


class Asesor(models.Model):
    Documento = models.CharField(max_length=12, null=False, blank=False)
    Nombres = models.CharField(max_length=50, null=False)
    ApellidoPaterno = models.CharField(max_length=50, null=False)
    ApellidoMaterno = models.CharField(max_length=50, blank=True)
    FechaNacimiento = models.DateField()
    Negocio = models.CharField(max_length=50)
    Cartera = models.CharField(max_length=50)
    Anexo = models.CharField(max_length=4)
    Telefono = models.CharField(max_length=20)
    Direccion = models.CharField(max_length=200)
    Sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    Jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE)
    Zonal = models.ForeignKey(Zonal, on_delete=models.CASCADE)
    TipoTrabajo = models.ForeignKey(TipoTrabajo, on_delete=models.CASCADE)
    Horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    Capacitador = models.ForeignKey(Capacitador, on_delete=models.CASCADE)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    FechaRegistro = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ['Documento', 'Nombres', 'ApelidoPaterno']


class Evaluaciones(models.Model):
    Asesor = models.ForeignKey(Asesor, on_delete=models.CASCADE)
    DocumentoCliente = models.CharField(max_length=12, null=False, blank=False)
    CodigoCentral = models.CharField(max_length=10)
    CodArchivo = models.CharField(max_length=60)
    ContactoDirecto = models.BooleanField(null=False)
    DetalleLlamada = models.CharField(max_length=500)
    Etapa = models.CharField(max_length=20)
    Capacitador = models.ForeignKey(Capacitador, on_delete=models.CASCADE)
    FechaEvaluacion = models.DateTimeField(null=False)
    FechaLlamada = models.DateTimeField(null=False)
    Feedback = models.BooleanField(null=False)
    FeedbackPendiente = models.BooleanField(null=False)
    Nota = models.FloatField(null=False)
    Observacion = models.CharField(max_length=500)
    TelefonoCliente = models.CharField(max_length=20)
    TipoGestion = models.CharField(max_length=100)
    AdvertenciaNoPago = models.CharField(max_length=10)
    AsumePDP = models.CharField(max_length=10)
    CaractInform = models.CharField(max_length=10)
    CierreCanalPago = models.CharField(max_length=10)
    ConsOfiAsist = models.CharField(max_length=10)
    ConsultaPago = models.CharField(max_length=10)
    DerivEncuesta = models.CharField(max_length=10)
    Despedida = models.CharField(max_length=10)
    Escuactiva = models.CharField(max_length=10)
    indagaClie = models.CharField(max_length=10)
    IndiGrab = models.CharField(max_length=10)
    MencionNegocio = models.CharField(max_length=10)
    MencionProducto = models.CharField(max_length=10)
    ModulaVoz = models.CharField(max_length=10)
    NoAsumePDP = models.CharField(max_length=10)
    Presenta = models.CharField(max_length=10)
    Saludo = models.CharField(max_length=10)
    TipiFinLlamada = models.CharField(max_length=10)
