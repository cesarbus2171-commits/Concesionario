from django.shortcuts import render
from django.http import HttpResponse

def proveedor(request):
    return render(request, 'proveedor/proveedor.html')
