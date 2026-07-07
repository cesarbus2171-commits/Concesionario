from django.db import models

class taller(models.Model):
    orden_reparacion = models.CharField(max_length=100)
    nombre_auto = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)
    servicio = models.CharField(max_length=200)
    mecanico = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=[('En proceso', 'En proceso'), ('Finalizado', 'Finalizado')], default='En proceso')
    class Meta:
        db_table = 'taller_taller'
