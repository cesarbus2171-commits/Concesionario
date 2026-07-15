from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from empleados.models import Empleado
from sucursal.models import Sucursal

def listaempleados(request):
    empleados = Empleado.objects.all()
    sucursales = Sucursal.objects.all()
    return render(request, 'empleados/empleados.html', {
        'empleados': empleados,
        'sucursales': sucursales
    })

def crear_empleado(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        puesto = request.POST.get('puesto')
        salario = request.POST.get('salario')
        fecha_contratacion = request.POST.get('fecha_contratacion')
        sucursal_id = request.POST.get('sucursal')
        estatus = request.POST.get('estatus', 'Activo')

        if not all([nombre, apellido, puesto, salario, fecha_contratacion, sucursal_id]):
            messages.error(request, 'Todos los campos son obligatorios.')
            return redirect('/empleados/')

        try:
            sucursal = Sucursal.objects.get(id=sucursal_id)
            nuevo_empleado = Empleado(
                nombre=nombre,
                apellido=apellido,
                puesto=puesto,
                salario=salario,
                fecha_contratacion=fecha_contratacion,
                sucursal=sucursal,
                estatus=estatus
            )
            nuevo_empleado.save()
            messages.success(request, 'Empleado agregado exitosamente.')
        except Sucursal.DoesNotExist:
            messages.error(request, 'La sucursal seleccionada no existe.')
        
        return redirect('/empleados/')
    return redirect('/empleados/')

def editar_empleado(request, id):
    empleado_edit = get_object_or_404(Empleado, id=id)
    
    if request.method == 'POST':
        empleado_edit.nombre = request.POST.get('nombre')
        empleado_edit.apellido = request.POST.get('apellido')
        empleado_edit.puesto = request.POST.get('puesto')
        empleado_edit.salario = request.POST.get('salario')
        empleado_edit.fecha_contratacion = request.POST.get('fecha_contratacion')
        empleado_edit.estatus = request.POST.get('estatus', 'Activo')
        
        sucursal_id = request.POST.get('sucursal')
        if sucursal_id:
            try:
                empleado_edit.sucursal = Sucursal.objects.get(id=sucursal_id)
            except Sucursal.DoesNotExist:
                messages.error(request, 'La sucursal seleccionada no existe.')
                return redirect('/empleados/')
                
        empleado_edit.save()
        messages.success(request, 'Empleado actualizado exitosamente.')
        return redirect('/empleados/')
        
    empleados = Empleado.objects.all()
    sucursales = Sucursal.objects.all()
    return render(request, 'empleados/empleados.html', {
        'empleados': empleados, 
        'sucursales': sucursales, 
        'empleado_edit': empleado_edit
    })

def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.delete()
    messages.success(request, 'Empleado eliminado exitosamente.')
    return redirect('/empleados/')