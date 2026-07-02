from django.shortcuts import render, redirect
from empleados.models import empleado

def listaempleados(request):
    empleados = empleado.objects.all()
    return render(request, 'empleados/empleados.html', {'empleados': empleados})

def crearempleado(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        puesto = request.POST['puesto']
        salario = request.POST['salario']
        fecha_contratacion = request.POST['fecha_contratacion']

        nuevo_empleado = empleado(nombre=nombre, apellido=apellido, puesto=puesto, salario=salario, fecha_contratacion=fecha_contratacion)
        nuevo_empleado.save()
        return redirect('/empleados/')