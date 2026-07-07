from django.db import models
from autos.models import Auto
from clientes.models import Cliente 

class Taller(models.Model):
    # Relaciones reales (Foreign Keys)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    # Datos específicos del taller
    orden_reparacion = models.CharField(max_length=100)
    servicio = models.CharField(max_length=200)
    mecanico = models.CharField(max_length=100)
    estado = models.CharField(
        max_length=20, 
        choices=[('En proceso', 'En proceso'), ('Finalizado', 'Finalizado')], 
        default='En proceso'
    )

    class Meta:
        db_table = 'taller_taller'

    def __str__(self):
        return f"Orden {self.orden_reparacion} - {self.auto.modelo}"