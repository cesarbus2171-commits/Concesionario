from django.shortcuts import redirect, render
from .models import venta

def listaventas(request):
    ventas = venta.objects.all()
    return render(request, 'ventas/ventas.html', {'ventas': ventas})

def crearventa(request):
    if request.method == 'POST':
        modelo_auto = request.POST['modelo_auto']
        cantidad = request.POST['cantidad']
        sucursal = request.POST['sucursal']
        fecha_venta = request.POST['fecha_venta']
        vendedor = request.POST['vendedor']


        nueva_venta = venta(modelo_auto=modelo_auto, cantidad=cantidad, sucursal=sucursal, fecha_venta=fecha_venta, vendedor=vendedor)
        nueva_venta.save()
        return redirect('/ventas/')