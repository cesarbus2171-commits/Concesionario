from django.urls import path
from .views import crearsucursal, listasucursal, editarsucursal, eliminarsucursal

urlpatterns = [
    path('', listasucursal, name='lista_sucursales'),
    path('nuevo/', crearsucursal, name='crear_sucursal'),
    path('editar/<int:id>/', editarsucursal, name='editar_sucursal'),
    path('eliminar/<int:id>/', eliminarsucursal, name='eliminar_sucursal'),
]