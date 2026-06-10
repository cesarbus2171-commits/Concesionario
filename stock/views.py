from django.shortcuts import render
from django.http import HttpResponse

def stock(request):
    return render(request, 'stock/stock.html')
