from django.db import models

class Venta(models.Model):
    auto = models.ForeignKey('autos.Auto', on_delete=models.CASCADE)
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    sucursal = models.ForeignKey('sucursal.Sucursal', on_delete=models.CASCADE)
    vendedor = models.ForeignKey('empleados.Empleado', on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=1)
    fecha_venta = models.DateField()
    estatus = models.CharField(max_length=20, default='Completada')

    class Meta:
        db_table = 'ventas_venta'

    def __str__(self):
        return f"Venta {self.id} - {self.auto.modelo}"