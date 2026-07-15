from django.urls import path
from .views import listaautos, crearauto, editarauto, eliminarauto

urlpatterns = [
    path('', listaautos, name='lista_autos'),
    path('nuevo/', crearauto, name='crear_auto'),
    path('editar/<int:id>/', editarauto, name='editar_auto'),
    path('eliminar/<int:id>/', eliminarauto, name='eliminar_auto'),
]