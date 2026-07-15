from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from fabrica.models import Fabrica

def listafabrica(request):
    fabricas = Fabrica.objects.all()
    return render(request, 'fabrica/fabrica.html', {'fabricas': fabricas})

def crearfabrica(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ubicacion = request.POST.get('ubicacion')
        capacidad_produccion = request.POST.get('capacidad_produccion')
        fecha_fundacion = request.POST.get('fecha_fundacion')
        procesos_activos = request.POST.get('procesos_activos')
        estatus = request.POST.get('estatus', 'Activo')

        nueva_fabrica = Fabrica(
            nombre=nombre, 
            ubicacion=ubicacion, 
            capacidad_produccion=capacidad_produccion, 
            fecha_fundacion=fecha_fundacion, 
            procesos_activos=procesos_activos,
            estatus=estatus
        )
        nueva_fabrica.save()
        messages.success(request, 'Fábrica registrada exitosamente.')
        return redirect('/fabrica/')
        
    return redirect('/fabrica/')

def editarfabrica(request, id):
    fabrica_edit = get_object_or_404(Fabrica, id=id)
    
    if request.method == 'POST':
        fabrica_edit.nombre = request.POST.get('nombre')
        fabrica_edit.ubicacion = request.POST.get('ubicacion')
        fabrica_edit.capacidad_produccion = request.POST.get('capacidad_produccion')
        fabrica_edit.fecha_fundacion = request.POST.get('fecha_fundacion')
        fabrica_edit.procesos_activos = request.POST.get('procesos_activos')
        fabrica_edit.estatus = request.POST.get('estatus', 'Activo')
        
        fabrica_edit.save()
        messages.success(request, 'Datos de la fábrica actualizados.')
        return redirect('/fabrica/')
        
    fabricas = Fabrica.objects.all()
    return render(request, 'fabrica/fabrica.html', {
        'fabricas': fabricas, 
        'fabrica_edit': fabrica_edit
    })

def eliminarfabrica(request, id):
    fabrica = get_object_or_404(Fabrica, id=id)
    fabrica.delete()
    messages.success(request, 'Fábrica eliminada del sistema.')
    return redirect('/fabrica/')