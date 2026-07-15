from django.urls import path
from .views import listaventas, crearventa, editarventa, eliminarventa

urlpatterns = [
    path('', listaventas, name='lista_ventas'),
    path('nuevo/', crearventa, name='crear_venta'),
    path('editar/<int:id>/', editarventa, name='editar_venta'),
    path('eliminar/<int:id>/', eliminarventa, name='eliminar_venta'),
]