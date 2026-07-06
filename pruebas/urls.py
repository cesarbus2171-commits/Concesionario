from django.urls import path
from .views import crearprueba, listapruebas

urlpatterns = [
    path('', listapruebas),
    path('nuevo/', crearprueba),
]