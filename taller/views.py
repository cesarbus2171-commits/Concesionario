from django.shortcuts import render, redirect, get_object_or_404
from .models import Taller

def listataller(request):
    return render(request, 'taller/taller.html', {'talleres': Taller.objects.all()})

def creartaller(request):
    if request.method == 'POST':
        Taller.objects.create(
            nombre=request.POST['nombre'],
            orden_reparacion=request.POST['orden_reparacion'],
            servicio=request.POST['servicio'],
            estado=request.POST['estado']
        )
        return redirect('/taller/')
    return redirect('/taller/')

def editartaller(request, id):
    taller_edit = get_object_or_404(Taller, id=id)
    if request.method == 'POST':
        taller_edit.nombre = request.POST['nombre']
        taller_edit.orden_reparacion = request.POST['orden_reparacion']
        taller_edit.servicio = request.POST['servicio']
        taller_edit.estado = request.POST['estado']
        taller_edit.save()
        return redirect('/taller/')
    return render(request, 'taller/taller.html', {'talleres': Taller.objects.all(), 'taller_edit': taller_edit})

def eliminartaller(request, id):
    get_object_or_404(Taller, id=id).delete()
    return redirect('/taller/')