from django.db import models

# Create your models here.
class Habitacion(models.Model):
    tipo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    desayuno_incluido = models.BooleanField(default=False)
    bano_privado = models.BooleanField(default=False)
    admite_mascotas = models.BooleanField(default=False)
    vista = models.CharField(max_length=100)