from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Habitacion(models.Model):
    tipo = models.CharField(max_length=100)
    capacidad = models.IntegerField(default=1)
    precio = models.IntegerField()
    desayuno_incluido = models.BooleanField(default=False)
    bano_privado = models.BooleanField(default=True)
    admite_mascotas = models.BooleanField(default=False)
    vista = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    calificacion = models.DecimalField(max_digits=3, decimal_places=2, default=5.00,validators=[MinValueValidator(1.00),MaxValueValidator(5.00)])
    imagen = models.ImageField(upload_to='imagenes_habitaciones/', null=True, blank=True)

    def __str__(self):
        return str(self.tipo)
    
class Reserva(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    habitacion = models.ForeignKey('Habitacion', on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva del {self.fecha_inicio} al {self.fecha_fin} para la habitación {self.habitacion}"

class Resena(models.Model):
    usuario = models.CharField(max_length=50)
    fecha = models.DateField()
    calificacion = models.DecimalField(max_digits=3, decimal_places=2, default=5.00,validators=[MinValueValidator(1.00),MaxValueValidator(5.00)])
    descripcion = models.CharField(max_length=200)
    habitacion = models.ForeignKey('Habitacion', on_delete=models.CASCADE)
    
    def __str__(self):
        return str (self.calificacion)