from django.urls import path
from .views import listaempleados, crear_empleado, editar_empleado, eliminar_empleado

urlpatterns = [
    path('', listaempleados, name='lista_empleados'),
    path('nuevo/', crear_empleado, name='crear_empleado'),
    # Rutas para modificar y eliminar
    path('editar/<int:id>/', editar_empleado, name='editar_empleado'),
    path('eliminar/<int:id>/', eliminar_empleado, name='eliminar_empleado'),
]