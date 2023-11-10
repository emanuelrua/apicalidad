from rest_framework import routers
from .views import *
from django.urls import path


router = routers.DefaultRouter()

router.register(r'asesores', AsesorViewSet)
router.register(r'capacitador', CapacitadorViewSet)
router.register(r'evaluaciones', EvaluacionesViewSet)
router.register(r'jornada', JornadaViewSet)
router.register(r'sexo', SexoViewSet)
router.register(r'zona', ZonalViewSet)
router.register(r'tipoTrabajo', TipoTrabajoViewSet)
router.register(r'horario', HorarioViewSet)
router.register(r'estado', EstadoViewSet)
router.register(r'cargo', CargoViewSet)


urlpatterns = router.urls
