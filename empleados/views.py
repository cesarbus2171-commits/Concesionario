from django.shortcuts import render
from django.http import HttpResponse

def empleados(request):

    return render(request, 'empleados/empleados.html')

# Create your views here.
