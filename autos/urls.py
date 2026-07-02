from django.urls import path
from .views import listaautos, crearauto

urlpatterns = [
    path('',listaautos),
    path('nuevo/',crearauto),
]