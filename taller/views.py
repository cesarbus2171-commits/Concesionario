from django.shortcuts import redirect, render
from .models import Taller
from autos.models import Auto
from clientes.models import Cliente


def listataller(request):
    talleres = Taller.objects.all()
    autos = Auto.objects.all()
    clientes = Cliente.objects.all()
    return render(request, 'Taller/taller.html', {'talleres': talleres, 'autos': autos, 'clientes': clientes})

def creartaller(request):
    if request.method == 'POST':
        auto_obj = Auto.objects.get(id=request.POST['auto'])
        cliente_obj = Cliente.objects.get(id=request.POST['cliente'])
    
        Taller.objects.create(
            orden_reparacion=request.POST['orden_reparacion'],
            auto=auto_obj,        # Asignas el objeto completo
            cliente=cliente_obj,  # Asignas el objeto completo
            servicio=request.POST['servicio'],
            mecanico=request.POST['mecanico'],
            estado=request.POST['estado']
        )
        return redirect('/taller/')