"""Modelos para la aplicación Mesa_de_Ayuda.

Contiene la definición de `Categoria` y `Solicitud`.

- Categoria: categorías posibles para clasificar solicitudes.
- Solicitud: entidad principal que representa una petición o ticket creada
  por un usuario del sistema.
"""

from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    """Modelo que representa una categoría para las solicitudes.

    Atributos:
        nombre (str): nombre único de la categoría.
        descripcion (str): texto opcional con más detalles.
    """

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        """Representación legible de la categoría (su nombre)."""
        return self.nombre


class Solicitud(models.Model):
    """Modelo que representa una solicitud (ticket) en la mesa de ayuda.

    Campos principales:
        titulo: texto corto con el título de la solicitud.
        descripcion: descripción breve del problema o petición.
        categoria: FK a `Categoria` para clasificar la solicitud.
        creador: FK al usuario que creó la solicitud.
        estado: estado actual del ticket (nueva, en_progreso, cerrada).
        prioridad: prioridad del ticket (low, med, high).
        fecha_creacion: fecha en que se creó la solicitud (auto_now_add).
        fecha_actualizacion: marca temporal de la última modificación (auto_now).
    """

    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)

    # elecciones para estado y prioridad; usar valores consistentes en la UI
    estado = models.CharField(
        choices=[('nueva', 'Nueva'), ('en_progreso', 'En Progreso'), ('cerrada', 'Cerrada')],
        max_length=50,
    )
    prioridad = models.CharField(
        choices=[('low', 'Baja'), ('med', 'Media'), ('high', 'Alta')],
        max_length=50,
    )

    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Cadena representativa de la solicitud: muestra el id y el título."""
        return f"{self.id} - {self.titulo}"