
# Register your models here.

from django.contrib import admin
from .models import Habitacion, Reserva, Resena, Pago, Profile

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'precio', 'desayuno_incluido', 'bano_privado', 'admite_mascotas', 'vista', 'disponible']
    
@admin.register(Reserva)   
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['cliente_id','fecha_inicio', 'fecha_fin', 'habitacion', 'estado_reserva', 'valor_reserva']

@admin.register(Resena)   
class ResenaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'fecha', 'calificacion', 'descripcion', 'habitacion']
    
@admin.register(Pago)   
class PagoAdmin(admin.ModelAdmin):
    list_display = ['id_reserva', 'tipo_pago', 'fecha_pago', 'monto','estado_pago']
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nombre_completo', 'direccion', 'correo', 'telefono')
    search_fields = ('user__username', 'nombre_completo')