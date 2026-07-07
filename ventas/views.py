from django.shortcuts import redirect, render
from .models import Venta
from clientes.models import Cliente
from autos.models import Auto

def listaventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/ventas.html', {'ventas': ventas})

def crearventa(request):
    if request.method == 'POST':
        # Buscamos las instancias reales usando los IDs enviados desde el formulario
        cliente_obj = Cliente.objects.get(id=request.POST['cliente_id'])
        auto_obj = Auto.objects.get(id=request.POST['auto_id'])
        
        Venta.objects.create(
            cliente=cliente_obj,
            auto=auto_obj,
            cantidad=request.POST['cantidad'],
            sucursal=request.POST['sucursal'],
            fecha_venta=request.POST['fecha_venta'],
            vendedor=request.POST['vendedor']
        )
        return redirect('/ventas/')
    return render(request, 'ventas/crear.html')