from datetime import datetime
from django.shortcuts import get_object_or_404, render
from .models import Habitacion, Resena
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reserva, Pago


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
        fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
        fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()

        habitaciones = habitaciones.exclude(
            id__in=Reserva.objects.filter(
                fecha_inicio__lt=fecha_fin,
                fecha_fin__gt=fecha_inicio
            ).values_list('habitacion_id', flat=True)
        )
    

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
    resenas = Resena.objects.all()
    habitacion_id = request.POST.get('habitacion_id')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    
    fecha_inicio = datetime.strptime(start_date, "%Y-%m-%d")
    fecha_termino = datetime.strptime(end_date, "%Y-%m-%d")
    dias_diferencia = (fecha_termino - fecha_inicio).days
    
    valor_total= (dias_diferencia*habitacion.precio)
    precio_total_formateado = f"{valor_total:,.0f}".replace(",", ".")
    precio_formateado = f"{habitacion.precio:,.0f}".replace(",", ".")
    limpieza = habitacion.valor_limpieza
    impuesto = int(valor_total)*habitacion.valor_impuesto
    total_reserva = (valor_total+limpieza+impuesto)
    limpieza_formateado = f"{limpieza:,.0f}".replace(",", ".")
    impuesto_formateado = f"{impuesto:,.0f}".replace(",", ".")
    valor_reserva = int(total_reserva)
    start_date_formateada = datetime.strptime(start_date, "%Y-%m-%d").strftime("%d-%m-%Y")
    end_date_formateada = datetime.strptime(end_date, "%Y-%m-%d").strftime("%d-%m-%Y")
    
    if not start_date or not end_date:
        return HttpResponse("Datos de fecha no encontrados.", status=400)
    if not habitacion_id:
        return HttpResponse("Datos de habitacion no encontrados.", status=400)
    
    return render(request, 'consulta.html', {
        'habitacion': habitacion,
        'start_date': start_date,
        'end_date': end_date,
        'start_date_formateada': start_date_formateada,
        'end_date_formateada': end_date_formateada,
        'dias_diferencia': dias_diferencia,
        'precio_formateado': precio_formateado,
        'precio_total_formateado': precio_total_formateado,
        'limpieza_formateado': limpieza_formateado,
        'impuesto_formateado': impuesto_formateado,
        'total_reserva': total_reserva,
        'valor_reserva': valor_reserva
    })
    
def guardar_reserva(request):
    if request.method == 'POST':
        cliente_id = request.user
        habitacion_id = request.POST.get('habitacion_id')
        fecha_inicio = request.POST.get('start_date')
        fecha_fin = request.POST.get('end_date')
        valor_reserva = request.POST.get('valor_reserva')

        print(f"ID de habitación: {habitacion_id}")  # Agregar para debug

        try:
            habitacion = Habitacion.objects.get(id=habitacion_id)
            
            nueva_reserva = Reserva(cliente_id=cliente_id, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, habitacion=habitacion, valor_reserva=valor_reserva)
            nueva_reserva.save()
            
            return render(request, 'pagar.html', {'reserva': nueva_reserva})
        except Habitacion.DoesNotExist:
            return HttpResponse("La habitación seleccionada no existe", status=400)
    else:
        return HttpResponse("Método no permitido.", status=405)

    
def guardar_pago(request):
    if request.method == 'POST':
        cliente_id = request.user
        reserva_id = request.POST.get('reserva_id')
        tipo_pago = request.POST.get('tipo_tarjeta')
        reserva = get_object_or_404(Reserva, id=reserva_id)
        monto = reserva.valor_reserva 

        nuevo_pago = Pago(cliente_id=cliente_id, id_reserva=reserva, tipo_pago=tipo_pago, monto=monto, estado_pago=True)
        nuevo_pago.save()
        
        return HttpResponse("Pago realizado con éxito.")
    return HttpResponse("Método no permitido.", status=405)