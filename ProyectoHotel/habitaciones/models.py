from django.db import models

# Create your models here.
class Habitacion(models.Model):
    tipo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    desayuno_incluido = models.BooleanField(default=False)
    bano_privado = models.BooleanField(default=True)
    admite_mascotas = models.BooleanField(default=False)
    vista = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='imagenes_habitaciones/', null=True, blank=True)

    def __str__(self):
        return self.tipo
    
class Reserva(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    habitacion = models.ForeignKey('Habitacion', on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva del {self.fecha_inicio} al {self.fecha_fin} para la habitación {self.habitacion}"