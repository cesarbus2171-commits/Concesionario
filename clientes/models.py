from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    tipo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    class Meta:
        db_table = 'clientes_cliente'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"