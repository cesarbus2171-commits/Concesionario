from django.urls import path
from .views import crearproveedor, listaproveedores

urlpatterns = [
    path('', listaproveedores),
    path('nuevo/', crearproveedor),
]