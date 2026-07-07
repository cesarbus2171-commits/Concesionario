from django.shortcuts import redirect, render
from .models import sucursal

def listasucursal(request):
    sucursales = sucursal.objects.all()
    return render(request, 'sucursal/sucursal.html', {'sucursales': sucursales})

def crearsucursal(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        ciudad = request.POST['ciudad']
        telefono = request.POST['telefono']

        nueva_sucursal = sucursal(nombre=nombre, direccion=direccion, ciudad=ciudad, telefono=telefono)
        nueva_sucursal.save()
        return redirect('/sucursal/')