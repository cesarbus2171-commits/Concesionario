from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente

def listaclientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes': clientes})

def crearcliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        sexo = request.POST.get('sexo')
        tipo = request.POST.get('tipo')
        direccion = request.POST.get('direccion')
        estatus = request.POST.get('estatus', 'Activo')

        nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, sexo=sexo, tipo=tipo, direccion=direccion, estatus=estatus)
        nuevo_cliente.save()
        return redirect('/clientes/')
        
    return redirect('/clientes/')

def editarcliente(request, id):
    cliente_edit = get_object_or_404(Cliente, id=id)
    
    if request.method == 'POST':
        cliente_edit.nombre = request.POST.get('nombre')
        cliente_edit.apellido = request.POST.get('apellido')
        cliente_edit.sexo = request.POST.get('sexo')
        cliente_edit.tipo = request.POST.get('tipo')
        cliente_edit.direccion = request.POST.get('direccion')
        cliente_edit.estatus = request.POST.get('estatus', 'Activo')
        cliente_edit.save()
        return redirect('/clientes/')
        
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {
        'clientes': clientes, 
        'cliente_edit': cliente_edit
    })

def eliminarcliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('/clientes/')