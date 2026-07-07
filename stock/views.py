from django.shortcuts import redirect, render
from .models import Stock
from autos.models import Auto
from fabrica.models import Fabrica
from proveedor.models import Proveedor

def listastock(request):
    # Definimos el contexto en una sola variable para mayor claridad
    context = {
        'stocks': Stock.objects.all(),
        'autos': Auto.objects.all(),
        'fabricas': Fabrica.objects.all(),
        'proveedores': Proveedor.objects.all(),
    }
    return render(request, 'stock/stock.html', context)

def crearstock(request):
    if request.method == 'POST':
        # Obtenemos los objetos relacionados
        auto_obj = Auto.objects.get(id=request.POST['auto_id'])
        fabrica_obj = Fabrica.objects.get(id=request.POST['fabrica_id'])
        proveedor_obj = Proveedor.objects.get(id=request.POST['proveedor_id'])
        
        # Guardamos el registro con todos los campos definidos en tu modelo
        Stock.objects.create(
            auto=auto_obj,
            fabrica=fabrica_obj,
            proveedor=proveedor_obj,
            cantidad=request.POST['cantidad'],
            fecha_ingreso=request.POST['fecha_ingreso'],
            ubicacion_bodega=request.POST['ubicacion_bodega'],
            disponibilidad=request.POST['disponibilidad']
        )
        return redirect('/stock/')
        
    return redirect('/stock/')