from django.db import models
from autos.models import Auto
from fabrica.models import Fabrica
from proveedor.models import Proveedor

class Stock(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_ingreso = models.DateField()
    ubicacion_bodega = models.CharField(max_length=100)
    disponibilidad = models.CharField(max_length=2, default='Sí')
    estatus = models.CharField(max_length=20, default='Activo')

    class Meta:
        db_table = 'stock_stock'

    def __str__(self):
        return f"{self.auto.marca} - {self.cantidad} unidades"