from django.shortcuts import render, redirect
from .models import Cliente

def listaclientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes': clientes})

def crearcliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        sexo = request.POST['sexo']
        tipo = request.POST['tipo']
        direccion = request.POST['direccion']

        nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, sexo=sexo, tipo=tipo, direccion=direccion)
        nuevo_cliente.save()
        return redirect('/clientes/')