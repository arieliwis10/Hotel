
# Register your models here.

from django.contrib import admin
from .models import Habitacion, Reserva, Resena

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'precio', 'desayuno_incluido', 'bano_privado', 'admite_mascotas', 'vista', 'disponible']
    
@admin.register(Reserva)   
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['fecha_inicio', 'fecha_fin', 'habitacion']

@admin.register(Resena)   
class ResenaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'fecha', 'calificacion', 'descripcion', 'habitacion']