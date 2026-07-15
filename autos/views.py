from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Auto

def listaautos(request):
    consultarautos = Auto.objects.all()
    return render(request, 'autos/autos.html', {'autos': consultarautos})

def crearauto(request):
    if request.method == 'POST':
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        anio = request.POST.get('anio')
        precio = request.POST.get('precio')
        edicion = request.POST.get('edicion')
        estatus = request.POST.get('estatus', 'Disponible')

        nuevo_auto = Auto(
            marca=marca, 
            modelo=modelo, 
            anio=anio, 
            precio=precio, 
            edicion=edicion,
            estatus=estatus
        )
        nuevo_auto.save()
        messages.success(request, 'Vehículo registrado en el inventario exitosamente.')
        return redirect('/autos/')
        
    return redirect('/autos/')

def editarauto(request, id):
    auto_edit = get_object_or_404(Auto, id=id)
    
    if request.method == 'POST':
        auto_edit.marca = request.POST.get('marca')
        auto_edit.modelo = request.POST.get('modelo')
        auto_edit.anio = request.POST.get('anio')
        auto_edit.precio = request.POST.get('precio')
        auto_edit.edicion = request.POST.get('edicion')
        auto_edit.estatus = request.POST.get('estatus', 'Disponible')
        
        auto_edit.save()
        messages.success(request, 'Datos del vehículo actualizados.')
        return redirect('/autos/')
        
    autos = Auto.objects.all()
    return render(request, 'autos/autos.html', {
        'autos': autos, 
        'auto_edit': auto_edit
    })

def eliminarauto(request, id):
    auto = get_object_or_404(Auto, id=id)
    auto.delete()
    messages.success(request, 'Vehículo eliminado del inventario.')
    return redirect('/autos/')