from rest_framework import routers
from .views import *
from django.urls import path,include
from . import views

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('users/', UserCreateView.as_view(), name='user-create'),  # URL para crear usuarios
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # URL para ver, actualizar o eliminar usuarios por ID
    path('asesor/', views.asesor, name='asesor-detail'), # URL para ver y cargar asesores
    path('asesor/<str:Documento>/', views.asesordni, name='asesor-detail'), #URL para ver detalles de asesor por DNI
    path('asesorupdate/<int:pk>/', views.asesor_update, name='asesorupdate'), #URL para editar asesores
    path('capacitador/', views.capacitador, name='capacitador'), # URL para consultar y cargar model capacitador
    path('capacitadorupdate/<int:pk>/', views.capacitador_update, name='capacitadorupdate'), #URL para  modificar capacitador
    path('evaluaciones/', views.evaluaciones, name='evaluaciones'), #URL consultar y cargar capacitaciones
    path('evaluacionesasesor/<int:asesor_id>/', views.evaluacionesasesor, name='evaluacionesasesor'), #URL Consultar evaluaciones ID asesor
    path('jornada/', views.jornada, name='jornada'),#URL consultar y cargar model jornada
    path('sexo/', views.sexo, name='sexo'), #URL para consultar y cargar model sexo
    path('zona/', views.zonal, name='zona'), #URL para consultar y cargar model zona
    path('tipotrabajo/', views.tipotrabajo, name='tipotrabajo'), # URL para consultar y cargar model tipotrabajo
    path('horario/', views.horario, name='horario'), #URL para consultar y cargar model horario
    path('estado/', views.estado, name='estado'), #URL para consultar y cargar model estado
    path('cargo/', views.cargo, name='cargo'), #URL para consultar y cargar model cargo
]