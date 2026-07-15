from django.urls import path
from .views import listapruebas, crearprueba, editarprueba, eliminarprueba

urlpatterns = [
    path('', listapruebas, name='lista_pruebas'),
    path('nuevo/', crearprueba, name='crear_prueba'),
    path('editar/<int:id>/', editarprueba, name='editar_prueba'),
    path('eliminar/<int:id>/', eliminarprueba, name='eliminar_prueba'),
]