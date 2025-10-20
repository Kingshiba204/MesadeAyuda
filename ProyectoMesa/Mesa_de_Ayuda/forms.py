"""Formularios del app Mesa_de_Ayuda.

Este módulo contiene los formularios basados en modelos usados para crear
y editar instancias de `Solicitud` en la aplicación.

Se mantiene el uso de `ModelForm` para aprovechar la validación y el
binding automático con los campos del modelo.
"""

from django import forms
from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    """Formulario para crear/editar objetos `Solicitud`.

    Este formulario expone los campos principales del modelo `Solicitud`:
    - titulo
    - descripcion
    - categoria
    - prioridad
    - estado

    Nota: La asociación del campo `creador` se realiza en la vista antes de guardar
    (commit=False) para asignar automáticamente el usuario que realiza la acción.
    """

    class Meta:
        model = Solicitud
        fields = ['titulo', 'descripcion', 'categoria', 'prioridad', 'estado']

