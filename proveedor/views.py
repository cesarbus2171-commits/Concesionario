from django.shortcuts import redirect, render
from .models import proveedor

def listaproveedores(request):
    provedores = proveedor.objects.all()
    return render(request, 'proveedor/proveedor.html', {'proveedores': provedores})

def crearproveedor(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        email = request.POST['email']
        productos_suministrados = request.POST['productos_suministrados']

        nuevo_proveedor = proveedor(nombre=nombre, direccion=direccion, telefono=telefono, email=email, productos_suministrados=productos_suministrados)
        nuevo_proveedor.save()
        return redirect('/proveedor/')