from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Sucursal

def listasucursal(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/sucursal.html', {'sucursales': sucursales})

def crearsucursal(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        ciudad = request.POST.get('ciudad')
        telefono = request.POST.get('telefono')
        estatus = request.POST.get('estatus', 'Activa')

        nueva_sucursal = Sucursal(
            nombre=nombre,
            direccion=direccion,
            ciudad=ciudad,
            telefono=telefono,
            estatus=estatus
        )
        nueva_sucursal.save()
        messages.success(request, 'Sucursal registrada exitosamente.')
        return redirect('/sucursal/')
        
    return redirect('/sucursal/')

def editarsucursal(request, id):
    sucursal_edit = get_object_or_404(Sucursal, id=id)
    
    if request.method == 'POST':
        sucursal_edit.nombre = request.POST.get('nombre')
        sucursal_edit.direccion = request.POST.get('direccion')
        sucursal_edit.ciudad = request.POST.get('ciudad')
        sucursal_edit.telefono = request.POST.get('telefono')
        sucursal_edit.estatus = request.POST.get('estatus', 'Activa')
        
        sucursal_edit.save()
        messages.success(request, 'Datos de la sucursal actualizados.')
        return redirect('/sucursal/')
        
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/sucursal.html', {
        'sucursales': sucursales, 
        'sucursal_edit': sucursal_edit
    })

def eliminarsucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    sucursal.delete()
    messages.success(request, 'Sucursal eliminada del sistema.')
    return redirect('/sucursal/')