from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def autos(request):

    return render(request, 'autos/autos.html')