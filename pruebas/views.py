from django.shortcuts import redirect, render
from .models import prueba

def listapruebas(request):
    pruebas = prueba.objects.all()
    return render(request, 'pruebas/pruebas.html', {'pruebas': pruebas})

def crearprueba(request):
    if request.method == 'POST':
        nombre_cliente = request.POST['nombre_cliente']
        fecha_prueba = request.POST['fecha_prueba']
        modelo_vehiculo = request.POST['modelo_vehiculo']
        empleado_encargado = request.POST['empleado_encargado']
        mecanico_asignado = request.POST['mecanico_asignado']

        nueva_prueba = prueba(nombre_cliente=nombre_cliente, fecha_prueba=fecha_prueba, modelo_vehiculo=modelo_vehiculo, empleado_encargado=empleado_encargado, mecanico_asignado=mecanico_asignado)
        nueva_prueba.save()
        return redirect('/pruebas/')