from django.shortcuts import render,redirect
from fabrica.models import fabrica

def listafabrica(request):
    fabricas = fabrica.objects.all()
    return render(request, 'fabrica/fabrica.html', {'fabricas': fabricas})

def crearfabrica(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        ubicacion = request.POST['ubicacion']
        capacidad_produccion = request.POST['capacidad_produccion']
        fecha_fundacion = request.POST['fecha_fundacion']
        procesos_activos = request.POST['procesos_activos']

        nueva_fabrica = fabrica(nombre=nombre, ubicacion=ubicacion, capacidad_produccion=capacidad_produccion, fecha_fundacion=fecha_fundacion, procesos_activos=procesos_activos)
        nueva_fabrica.save()
        return redirect('/fabrica/')
