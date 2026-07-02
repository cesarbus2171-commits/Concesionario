from django.urls import path
from .views import crearcliente, listaclientes

urlpatterns = [
    path('', listaclientes),
    path('nuevo/', crearcliente),
]