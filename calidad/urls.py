from rest_framework import routers
from .views import *
from django.urls import path


router = routers.DefaultRouter()

router.register(r'asesores', AsesorViewSet)
router.register(r'capacitador', CapacitadorViewSet)
router.register(r'evaluaciones', EvaluacionesViewSet)

urlpatterns = router.urls