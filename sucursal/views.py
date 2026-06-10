from django.shortcuts import render
from django.http import HttpResponse

def sucursal(request):
    return render(request, 'sucursal/sucursal.html')
