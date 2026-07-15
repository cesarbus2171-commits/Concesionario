from django.db import models

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    estatus = models.CharField(max_length=20, default='Activo')

    class Meta:
        db_table = 'sucursal_sucursal'

    def __str__(self):
        return self.nombre