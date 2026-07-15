from django.db import models
from sucursal.models import Sucursal

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField()
    sucursal = models.ForeignKey('sucursal.Sucursal', on_delete=models.CASCADE, related_name='empleados')
    estatus = models.CharField(max_length=20, default='Activo')

    class Meta:
        db_table = 'empleados_empleados'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"