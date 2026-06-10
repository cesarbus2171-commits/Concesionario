from django.shortcuts import render
from django.http import HttpResponse

def ventas(request):
    return render(request, 'ventas/ventas.html')

# Create your views here.
