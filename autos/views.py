from django.shortcuts import render, redirect
from .models import Auto

def listaautos(request):
    consultarautos = Auto.objects.all()
    # CAMBIO AQUÍ: Cambiamos 'consultarautos' por 'autos' para que coincida con tu {% for auto in autos %}
    return render(request, 'autos/autos.html', {'autos': consultarautos})

# Tu función de crear se queda exactamente igual a como la tienes
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