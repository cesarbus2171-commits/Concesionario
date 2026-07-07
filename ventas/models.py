from django.db import models

class venta(models.Model):
    modelo_auto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    sucursal = models.CharField(max_length=100)
    fecha_venta = models.DateField()
    vendedor = models.CharField(max_length=100)
    class Meta:
        db_table = 'ventas_venta'
