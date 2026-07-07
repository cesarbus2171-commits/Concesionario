from django.db import models
from clientes.models import Cliente
from autos.models import Auto

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    sucursal = models.CharField(max_length=100)
    fecha_venta = models.DateField()
    vendedor = models.CharField(max_length=100)

    class Meta:
        db_table = 'ventas_venta'