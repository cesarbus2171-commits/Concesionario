from django.urls import path
from .views import listataller, creartaller, editartaller, eliminartaller

urlpatterns = [
    path('', listataller, name='lista_taller'),
    path('nuevo/', creartaller, name='crear_taller'),
    path('editar/<int:id>/', editartaller, name='editar_taller'),
    path('eliminar/<int:id>/', eliminartaller, name='eliminar_taller'),
]