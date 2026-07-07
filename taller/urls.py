from django.urls import path
from .views import creartaller, listataller

urlpatterns = [
    path('', listataller),
    path('nuevo/', creartaller),
]