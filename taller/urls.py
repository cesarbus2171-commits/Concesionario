from django.urls import path
from . import views

urlpatterns = [
    path('form-taller', views.taller),
]