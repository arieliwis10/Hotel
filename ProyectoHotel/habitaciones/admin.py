
# Register your models here.

from django.contrib import admin
from .models import Habitacion

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'precio', 'desayuno_incluido', 'bano_privado', 'admite_mascotas', 'vista', 'disponible']
