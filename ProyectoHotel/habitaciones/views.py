from django.shortcuts import get_object_or_404, render
from .models import Habitacion
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reserva

# Create your views here.

def home(request):
    return render(request, 'home.html')

def habitaciones(request):
    habitaciones = Habitacion.objects.all()  # Obtener todas las habitaciones de la base de datos
    return render(request, 'habitaciones.html', {'habitaciones': habitaciones})


def mostrar_calendario(request):
    reservas = Reserva.objects.all()
    fechas_reservadas = []
    
    for reserva in reservas:
        fechas_reservadas.append({
            "from": reserva.fecha_inicio.strftime("%Y-%m-%d"),
            "to": reserva.fecha_fin.strftime("%Y-%m-%d")
        })
    
    return render(request, 'tu_plantilla.html', {
        'fechas_reservadas': fechas_reservadas
    })

def reservas(request):
    
        
        return render(request, 'reservas.html')