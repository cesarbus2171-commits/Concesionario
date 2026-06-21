from django.db import models

class fabrica(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    capacidad_produccion = models.IntegerField()
    fecha_fundacion = models.DateField()
    procesos_activos = models.CharField(max_length=200)