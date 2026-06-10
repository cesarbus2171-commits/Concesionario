from django.urls import path
from . import views

urlpatterns = [
    path('form-fabrica', views.fabrica),
]