from django.shortcuts import render
from django.http import HttpResponse

def pruebas(request):

    return render(request, 'pruebas/pruebas.html')
