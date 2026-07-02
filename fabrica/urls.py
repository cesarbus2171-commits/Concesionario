from django.urls import path
from .views import listafabrica, crearfabrica   

urlpatterns = [
    path('', listafabrica),
    path('crear/', crearfabrica),
]