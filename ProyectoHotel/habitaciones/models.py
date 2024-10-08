from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    nombre_completo = models.CharField(max_length=255, blank=True)
    correo = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.user.username

class Habitacion(models.Model):
    tipo = models.CharField(max_length=100)
    capacidad = models.IntegerField(default=1)
    precio = models.IntegerField()
    desayuno_incluido = models.BooleanField(default=False)
    bano_privado = models.BooleanField(default=True)
    admite_mascotas = models.BooleanField(default=False)
    vista = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    valor_limpieza = models.IntegerField(default=12000)
    valor_impuesto = models.DecimalField(max_digits=4, decimal_places=2,default=0.05)
    calificacion = models.DecimalField(max_digits=3, decimal_places=2, default=5.00,validators=[MinValueValidator(1.00),MaxValueValidator(5.00)])
    imagen = models.ImageField(upload_to='imagenes_habitaciones/', null=True, blank=True)

    def __str__(self):
        return str(self.tipo)
    
class Reserva(models.Model):
    cliente_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    habitacion = models.ForeignKey('Habitacion', on_delete=models.CASCADE)
    id_pago = models.BooleanField(default= False)
    estado_reserva = models.CharField(max_length=200, default="Pendiente") #Pendiente,Pagado, Habitada
    #cambiar estado_reserva cuando se realice el Check-In y cuando se pague
    valor_reserva = models.IntegerField(default=0)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    def __str__(self):
        return str(self.cliente_id.username)

class Pago(models.Model):
    cliente_id = models.ForeignKey(User, on_delete=models.CASCADE)
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    tipo_pago = models.CharField(max_length=100)
    fecha_pago = models.DateField(default=timezone.now)
    monto = models.IntegerField(default=0)
    estado_pago = models.BooleanField(default=False)
    
    def __str__(self):
        return str (self.estado_pago)
    

class Resena(models.Model):
    usuario = models.CharField(max_length=50)
    fecha = models.DateField()
    calificacion = models.DecimalField(max_digits=3, decimal_places=2, default=5.00,validators=[MinValueValidator(1.00),MaxValueValidator(5.00)])
    descripcion = models.CharField(max_length=200)
    habitacion = models.ForeignKey('Habitacion', on_delete=models.CASCADE)
    
    def __str__(self):
        return str (self.calificacion)
    
#usuarios: juan , pass:Juan1234 , naty, pass:Nataly1234