from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Venta
from autos.models import Auto
from clientes.models import Cliente
from sucursal.models import Sucursal
from empleados.models import Empleado

def listaventas(request):
    return render(request, 'ventas/ventas.html', {
        'ventas': Venta.objects.all(),
        'autos': Auto.objects.all(),
        'clientes': Cliente.objects.all(),
        'sucursales': Sucursal.objects.all(),
        'empleados': Empleado.objects.all()
    })

def crearventa(request):
    if request.method == 'POST':
        Venta.objects.create(
            auto_id=request.POST['auto_id'],
            cliente_id=request.POST['cliente_id'],
            sucursal_id=request.POST['sucursal_id'],
            vendedor_id=request.POST.get('vendedor_id') or None,
            cantidad=request.POST['cantidad'],
            fecha_venta=request.POST['fecha_venta'],
            estatus=request.POST.get('estatus', 'Completada')
        )
        messages.success(request, 'Venta registrada.')
        return redirect('/ventas/')
    return redirect('/ventas/')

def editarventa(request, id):
    venta_edit = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        venta_edit.auto_id = request.POST['auto_id']
        venta_edit.cliente_id = request.POST['cliente_id']
        venta_edit.sucursal_id = request.POST['sucursal_id']
        venta_edit.vendedor_id = request.POST.get('vendedor_id') or None
        venta_edit.cantidad = request.POST['cantidad']
        venta_edit.fecha_venta = request.POST['fecha_venta']
        venta_edit.estatus = request.POST.get('estatus', 'Completada')
        venta_edit.save()
        return redirect('/ventas/')
        
    return render(request, 'ventas/ventas.html', {
        'ventas': Venta.objects.all(),
        'autos': Auto.objects.all(),
        'clientes': Cliente.objects.all(),
        'sucursales': Sucursal.objects.all(),
        'empleados': Empleado.objects.all(),
        'venta_edit': venta_edit
    })

def eliminarventa(request, id):
    get_object_or_404(Venta, id=id).delete()
    return redirect('/ventas/')