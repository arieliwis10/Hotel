from django.shortcuts import get_object_or_404, render
from .models import Habitacion
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reserva


def home(request):
    return render(request, 'home.html')

def habitaciones(request):
    tipo = request.GET.get('tipo', '')
    capacidad = request.GET.get('capacidad', '')  
    fecha_inicio = request.GET.get('start_date', None)
    fecha_fin = request.GET.get('end_date', None)

    habitaciones = Habitacion.objects.all()

    if tipo:
        habitaciones = habitaciones.filter(tipo=tipo)
    if capacidad:
        habitaciones = habitaciones.filter(capacidad__gte=capacidad)
    if fecha_inicio and fecha_fin:
        pass  

    tipos_disponibles = Habitacion.objects.values_list('tipo', flat=True).distinct()
    capacidades_disponibles = Habitacion.objects.values_list('capacidad', flat=True).distinct().order_by('capacidad')

    return render(request, 'habitaciones.html', {
        'habitaciones': habitaciones,
        'tipo': tipo,
        'capacidad': capacidad,
        'tipos_disponibles': tipos_disponibles,
        'capacidades_disponibles': capacidades_disponibles,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
    })

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

def consultar_reserva(request):
    habitacion_id = request.POST.get('habitacion_id')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)

    if not start_date or not end_date:
        return HttpResponse("Datos de fecha no encontrados.", status=400)
    if not habitacion_id:
        return HttpResponse("Datos de habitacion no encontrados.", status=400)
    
    return render(request, 'consulta.html', {
        'habitacion': habitacion,
        'start_date': start_date,
        'end_date': end_date
    })