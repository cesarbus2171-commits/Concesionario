from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Stock
from autos.models import Auto
from fabrica.models import Fabrica
from proveedor.models import Proveedor

def listastock(request):
    return render(request, 'stock/stock.html', {
        'stocks': Stock.objects.all(),
        'autos': Auto.objects.all(),
        'fabricas': Fabrica.objects.all(),
        'proveedores': Proveedor.objects.all()
    })

def crearstock(request):
    if request.method == 'POST':
        Stock.objects.create(
            auto_id=request.POST['auto_id'],
            fabrica_id=request.POST['fabrica_id'],
            proveedor_id=request.POST['proveedor_id'],
            cantidad=request.POST['cantidad'],
            fecha_ingreso=request.POST['fecha_ingreso'],
            ubicacion_bodega=request.POST['ubicacion_bodega'],
            estatus=request.POST.get('estatus', 'Activo')
        )
        messages.success(request, 'Stock registrado.')
        return redirect('/stock/')
    return redirect('/stock/')

def editarstock(request, id):
    stock_edit = get_object_or_404(Stock, id=id)
    if request.method == 'POST':
        stock_edit.auto_id = request.POST['auto_id']
        stock_edit.fabrica_id = request.POST['fabrica_id']
        stock_edit.proveedor_id = request.POST['proveedor_id']
        stock_edit.cantidad = request.POST['cantidad']
        stock_edit.fecha_ingreso = request.POST['fecha_ingreso']
        stock_edit.ubicacion_bodega = request.POST['ubicacion_bodega']
        stock_edit.estatus = request.POST.get('estatus', 'Activo')
        stock_edit.save()
        return redirect('/stock/')
    return render(request, 'stock/stock.html', {
        'stocks': Stock.objects.all(), 'autos': Auto.objects.all(),
        'fabricas': Fabrica.objects.all(), 'proveedores': Proveedor.objects.all(),
        'stock_edit': stock_edit
    })

def eliminarstock(request, id):
    get_object_or_404(Stock, id=id).delete()
    return redirect('/stock/')