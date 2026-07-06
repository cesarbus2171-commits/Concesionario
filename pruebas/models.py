from django.db import models

class prueba(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    fecha_prueba = models.DateField()
    modelo_vehiculo = models.CharField(max_length=100)
    empleado_encargado = models.CharField(max_length=100)
    mecanico_asignado = models.CharField(max_length=100)

    class Meta:
        db_table = 'pruebas_pruebas'
