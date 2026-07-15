from django.urls import path
from .views import listafabrica, crearfabrica, editarfabrica, eliminarfabrica

urlpatterns = [
    path('', listafabrica, name='lista_fabricas'),
    path('crear/', crearfabrica, name='crear_fabrica'),
    # Nuevas rutas para el CRUD
    path('editar/<int:id>/', editarfabrica, name='editar_fabrica'),
    path('eliminar/<int:id>/', eliminarfabrica, name='eliminar_fabrica'),
]