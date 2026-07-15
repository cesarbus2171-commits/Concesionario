from django.db import models

class Prueba(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    fecha_prueba = models.DateField()
    autos = models.ManyToManyField('autos.Auto', related_name='pruebas')
    empleado_encargado = models.ForeignKey('empleados.Empleado', on_delete=models.SET_NULL, null=True)
    taller_asignado = models.ForeignKey('taller.Taller', on_delete=models.SET_NULL, null=True, related_name='pruebas')
    sucursal = models.ForeignKey('sucursal.Sucursal', on_delete=models.CASCADE, null=True)
    estatus = models.CharField(max_length=20, default='Programada')

    def __str__(self):
        return f"Prueba de {self.nombre_cliente} - {self.fecha_prueba}"