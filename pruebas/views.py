from django.shortcuts import render, redirect, get_object_or_404
from .models import Prueba
from taller.models import Taller
from autos.models import Auto
from empleados.models import Empleado
from sucursal.models import Sucursal

def listapruebas(request):
    return render(request, 'pruebas/pruebas.html', {
        'pruebas': Prueba.objects.all(),
        'autos': Auto.objects.all(),
        'empleados': Empleado.objects.all(),
        'talleres': Taller.objects.all(),
        'sucursales': Sucursal.objects.all()
    })

def crearprueba(request):
    if request.method == 'POST':
        nueva = Prueba.objects.create(
            nombre_cliente=request.POST['nombre_cliente'],
            fecha_prueba=request.POST['fecha_prueba'],
            empleado_encargado_id=request.POST['empleado_encargado_id'],
            taller_asignado_id=request.POST['taller_asignado_id'],
            sucursal_id=request.POST['sucursal_id']
        )
        nueva.autos.set(request.POST.getlist('autos'))
        return redirect('/pruebas/')
    return redirect('/pruebas/')

def editarprueba(request, id):
    prueba_edit = get_object_or_404(Prueba, id=id)
    if request.method == 'POST':
        prueba_edit.nombre_cliente = request.POST['nombre_cliente']
        prueba_edit.fecha_prueba = request.POST['fecha_prueba']
        prueba_edit.empleado_encargado_id = request.POST['empleado_encargado_id']
        prueba_edit.mecanico_asignado_id = request.POST['mecanico_asignado_id']
        prueba_edit.sucursal_id = request.POST['sucursal_id']
        prueba_edit.estatus = request.POST.get('estatus', 'Programada')
        prueba_edit.save()
        prueba_edit.autos.set(request.POST.getlist('autos'))
        return redirect('/pruebas/')
    
    return render(request, 'pruebas/pruebas.html', {
        'pruebas': Prueba.objects.all(),
        'autos': Auto.objects.all(),
        'empleados': Empleado.objects.all(),
        'sucursales': Sucursal.objects.all(),
        'prueba_edit': prueba_edit
    })

def eliminarprueba(request, id):
    get_object_or_404(Prueba, id=id).delete()
    return redirect('/pruebas/')