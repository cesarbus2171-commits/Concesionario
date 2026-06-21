from django.db import models


class cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField()
    sexo = models.CharField()
    tipo = models.CharField()
    direccion = models.CharField()