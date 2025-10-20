from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.contrib.auth import logout 
from .models import Solicitud, Categoria
from .forms import SolicitudForm
from django.db.models import Q

@login_required
def home(request):
    solicitudes = Solicitud.objects.filter(Q(creador=request.user) | Q(creador__is_superuser=True)).select_related('categoria','creador')
    estado_filtro = request.GET.get('estado')
    if estado_filtro:
        solicitudes = solicitudes.filter(estado=estado_filtro)
        request.session['filtros'] = {'estado': estado_filtro} 

    return render(request, 'home.html', {'solicitudes': solicitudes})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid(): 
            solicitud = form.save(commit=False)
            solicitud.creador = request.user 
            solicitud.save()
            if hasattr(form, 'save_m2m'):
                form.save_m2m()
            messages.success(request, '¡Solicitud creada exitosamente!') 
            return redirect('home')
        return render(request, 'solicitud_form.html', {'form': form, 'titulo_pagina': 'Nueva Solicitud'})
    else:
        form = SolicitudForm()
    
    return render(request, 'solicitud_form.html', {'form': form, 'titulo_pagina': 'Nueva Solicitud'})

@login_required
def editar_solicitud(request, pk): 
    solicitud = get_object_or_404(Solicitud, pk=pk)

    if not (request.user.is_superuser or solicitud.creador == request.user):
        messages.error(request, 'No tienes permiso para editar esta solicitud.')
        return redirect('home')

    if request.method == 'POST':
        form = SolicitudForm(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Solicitud actualizada!')
            return redirect('home')
    else:
        form = SolicitudForm(instance=solicitud)

    return render(request, 'solicitud_form.html', {'form': form, 'titulo_pagina': 'Editar Solicitud'})


@login_required
def eliminar_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)

    if not (request.user.is_superuser or solicitud.creador == request.user):
        messages.error(request, 'No tienes permiso para eliminar esta solicitud.')
        return redirect('home')

    if request.method == 'POST':
        solicitud.delete()
        messages.success(request, 'Solicitud eliminada correctamente.')
        return redirect('home')

    return render(request, 'confirm_delete.html', {'solicitud': solicitud})