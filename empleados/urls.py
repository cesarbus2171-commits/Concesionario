from django.urls import path
from .views import listaempleados, crearempleado

urlpatterns = [
    path('', listaempleados),
    path('nuevo/', crearempleado),
]