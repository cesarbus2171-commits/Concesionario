from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Proveedor

def listaproveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/proveedor.html', {'proveedores': proveedores})

def crearproveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        productos_suministrados = request.POST.get('productos_suministrados')
        estatus = request.POST.get('estatus', 'Activo')

        nuevo_proveedor = Proveedor(
            nombre=nombre, 
            direccion=direccion, 
            telefono=telefono, 
            email=email, 
            productos_suministrados=productos_suministrados,
            estatus=estatus
        )
        nuevo_proveedor.save()
        messages.success(request, 'Proveedor registrado exitosamente.')
        return redirect('/proveedor/')
        
    return redirect('/proveedor/')

# --- MODIFICADO: EDITAR PROVEEDOR EN LA MISMA PÁGINA ---
def editarproveedor(request, id):
    # Buscamos el proveedor a editar
    proveedor_edit = get_object_or_404(Proveedor, id=id)
    
    if request.method == 'POST':
        proveedor_edit.nombre = request.POST.get('nombre')
        proveedor_edit.direccion = request.POST.get('direccion')
        proveedor_edit.telefono = request.POST.get('telefono')
        proveedor_edit.email = request.POST.get('email')
        proveedor_edit.productos_suministrados = request.POST.get('productos_suministrados')
        proveedor_edit.estatus = request.POST.get('estatus', 'Activo')
        
        proveedor_edit.save()
        messages.success(request, 'Datos del proveedor actualizados.')
        return redirect('/proveedor/')
        
    # Si es GET, cargamos LA MISMA PÁGINA principal
    # Pero le mandamos la lista completa (para la tabla) y el proveedor_edit (para el formulario)
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/proveedor.html', {
        'proveedores': proveedores, 
        'proveedor_edit': proveedor_edit
    })

def eliminarproveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    messages.success(request, 'Proveedor eliminado del sistema.')
    return redirect('/proveedor/')