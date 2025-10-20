"""Rutas (URLs) del app Mesa_de_Ayuda.

Define las rutas utilizadas para listar, crear, editar y eliminar
solicitudes (tickets).
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear_solicitud/', views.crear_solicitud, name='crear_solicitud'),
    path('solicitud/editar/<int:pk>/', views.editar_solicitud, name='editar_solicitud'),
    path('solicitud/<int:pk>/eliminar/', views.eliminar_solicitud, name='eliminar_solicitud'),
]