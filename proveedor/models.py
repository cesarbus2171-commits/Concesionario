from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    productos_suministrados = models.TextField()
    class Meta:
        db_table = 'proveedor_proveedor'
