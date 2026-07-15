from django.urls import path
from .views import listastock, crearstock, editarstock, eliminarstock

urlpatterns = [
    path('', listastock, name='lista_stock'),
    path('nuevo/', crearstock, name='crear_stock'),
    path('editar/<int:id>/', editarstock, name='editar_stock'),
    path('eliminar/<int:id>/', eliminarstock, name='eliminar_stock'),
]