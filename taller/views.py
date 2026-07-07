from django.shortcuts import redirect, render
from .models import taller

def listataller(request):
    talleres = taller.objects.all()
    return render(request, 'taller/taller.html', {'talleres': talleres})

def creartaller(request):
    if request.method == 'POST':
        orden_reparacion = request.POST['orden_reparacion']
        nombre_auto = request.POST['nombre_auto']
        cliente = request.POST['cliente']
        servicio = request.POST['servicio']
        mecanico = request.POST['mecanico']
        estado = request.POST['estado']

        nuevo_taller = taller(orden_reparacion=orden_reparacion, nombre_auto=nombre_auto, cliente=cliente, servicio=servicio, mecanico=mecanico, estado=estado)
        nuevo_taller.save()
        return redirect('/taller/')