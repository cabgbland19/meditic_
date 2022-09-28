from django.urls import path
from .Api.api import CiudadAPIView
from .Api.api import GeneroAPIView
from .Api.api import EspecialidadAPIView
from .Api.api import RolAPIView
from .Api.api import PacienteAPIView
from .Api.api import MedicoAPIView
from .Api.api import FamiliarAPIView
from .Api.api import UsuarioAPIView
from .Api.api import editbyid

""" . importa del paquete actual (apiUsers) - Cami"""
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('Ciudad/',CiudadAPIView.as_view(), name ='Ciudad_api'),
    path('Genero/',GeneroAPIView.as_view(), name = 'Genero_api'),
    path('Especialidad/',EspecialidadAPIView.as_view(), name = 'Especialidad_api'),
    path('Rol/',RolAPIView.as_view(), name = 'Rol_api'),
    path('Paciente/',PacienteAPIView.as_view(), name = 'Paciente_api'),
    path('Paciente/<int:patient_id>/',editbyid, name = 'Paciente_api_id'),
    path('Medico/',MedicoAPIView.as_view(), name = 'Medico_api'),
    path('Familiar/',FamiliarAPIView.as_view(), name = 'Familiar_api'),
    path('Usuario/',UsuarioAPIView.as_view(), name = 'Usuario_api'),
]

