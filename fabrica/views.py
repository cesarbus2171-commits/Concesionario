from django.shortcuts import render
from django.http import HttpResponse

def fabrica(request):

    return render(request, 'fabrica/fabrica.html')

# Create your views here.
