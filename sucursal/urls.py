from django.urls import path
from .views import crearsucursal, listasucursal

urlpatterns = [
    path('', listasucursal),
    path('nuevo/', crearsucursal),
]