from django.shortcuts import redirect, render
from .models import stock

def listastock(request):
    stocks = stock.objects.all()
    return render(request, 'stock/stock.html', {'stocks': stocks})

def crearstock(request):
    if request.method == 'POST':
        modelo_auto = request.POST['modelo_auto']
        cantidad = request.POST['cantidad']
        sucursal = request.POST['sucursal']
        fecha_ingreso = request.POST['fecha_ingreso']
        disponibilidad = request.POST['disponibilidad']



        nuevo_stock = stock(modelo_auto=modelo_auto, cantidad=cantidad, sucursal=sucursal, fecha_ingreso=fecha_ingreso, disponibilidad=disponibilidad)
        nuevo_stock.save()
        return redirect('/stock/')