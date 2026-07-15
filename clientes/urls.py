from django.urls import path
from .views import crearcliente, listaclientes, editarcliente, eliminarcliente

urlpatterns = [
    path('', listaclientes, name='lista_clientes'),
    path('nuevo/', crearcliente, name='crear_cliente'),
    # Nuevas rutas para modificar y eliminar
    path('editar/<int:id>/', editarcliente, name='editar_cliente'),
    path('eliminar/<int:id>/', eliminarcliente, name='eliminar_cliente'),
]