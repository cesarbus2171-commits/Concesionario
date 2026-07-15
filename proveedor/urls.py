from django.urls import path
from .views import crearproveedor, listaproveedores, editarproveedor, eliminarproveedor

urlpatterns = [
    path('', listaproveedores, name='lista_proveedores'),
    path('nuevo/', crearproveedor, name='crear_proveedor'),
    # Nuevas rutas para el CRUD
    path('editar/<int:id>/', editarproveedor, name='editar_proveedor'),
    path('eliminar/<int:id>/', eliminarproveedor, name='eliminar_proveedor'),
]