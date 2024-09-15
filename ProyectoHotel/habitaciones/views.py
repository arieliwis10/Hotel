from django.shortcuts import render
from .models import Habitacion

# Create your views here.

def home(request):
    return render(request, 'home.html')

def habitaciones(request):
    return render(request, 'habitaciones.html')

