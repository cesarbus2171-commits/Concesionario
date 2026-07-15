from django.db import models

class Taller(models.Model):
    nombre = models.CharField(max_length=100, default="Taller Central")
    orden_reparacion = models.CharField(max_length=50)
    servicio = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, default='En proceso')
    estatus = models.CharField(max_length=20, default='Activo')

    class Meta:
        db_table = 'taller_taller'

    def __str__(self):
        return self.nombre