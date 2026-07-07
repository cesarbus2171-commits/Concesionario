from django.urls import path
from .views import crearstock, listastock

urlpatterns = [
    path('', listastock),
    path('nuevo/', crearstock),
]