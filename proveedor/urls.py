from django.urls import path
from . import views

urlpatterns = [
    path('form-proveedor', views.proveedor),
]