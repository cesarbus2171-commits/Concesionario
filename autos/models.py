from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    edicion = models.CharField(max_length=100)

    class Meta:
        db_table = 'autos_auto'

    def __str__(self):
        return f"{self.marca} {self.modelo}"