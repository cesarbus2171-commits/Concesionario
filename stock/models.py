from django.db import models

class stock(models.Model):
    modelo_auto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    sucursal = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    disponibilidad = models.CharField(max_length=2, choices=[('Si', 'Si'), ('No', 'No')], default='Si')

    class Meta:
        db_table = 'stock_stock'
