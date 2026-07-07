from django.urls import path
from .views import crearventa, listaventas

urlpatterns = [
    path('', listaventas),
    path('nuevo/', crearventa),
]