"""Registro de modelos en el admin de Django para Mesa_de_Ayuda.

Aquí registramos `Categoria` y `Solicitud` para que sean gestionables
desde el panel de administración. Los admin básicos se usan en desarrollo
para facilitar la inspección de datos.
"""

from django.contrib import admin
from .models import Categoria, Solicitud


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	"""Configuración mínima del admin para `Categoria`."""
	list_display = ('id', 'nombre')
	search_fields = ('nombre',)


@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
	"""Configuración mínima del admin para `Solicitud`."""
	list_display = ('id', 'titulo', 'creador', 'categoria', 'estado', 'prioridad')
	list_filter = ('estado', 'prioridad', 'categoria')
	search_fields = ('titulo', 'descripcion')
