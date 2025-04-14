from django.db import models

class Gasto(models.Model):
    nombre = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50, default='General')
    fecha = models.DateField()

    def __str__(self):
        return f"{self.nombre} - ${self.monto}"
