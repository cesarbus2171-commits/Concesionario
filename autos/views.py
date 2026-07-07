from django.shortcuts import render, redirect
from .models import Auto

def listaautos(request):
    consultarautos = Auto.objects.all()
    return render(request, 'autos/autos.html', {'autos': consultarautos})

def crearauto(request):
    if request.method == 'POST':
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        anio = request.POST['anio']
        precio = request.POST['precio']
        edicion = request.POST['edicion']

        nuevo_auto = Auto(marca=marca, modelo=modelo, anio=anio, precio=precio, edicion=edicion)
        nuevo_auto.save()
        return redirect('/autos/')