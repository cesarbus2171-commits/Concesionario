from django.shortcuts import render
from django.http import HttpResponse

def taller(request):
    return render(request, 'taller/taller.html')

# Create your views here.
