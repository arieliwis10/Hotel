# usuarios/urls.py
from django.urls import path
from .views import registro, iniciar_sesion, cerrar_sesion, perfil_usuario, registro

urlpatterns = [
    path("registro/", registro, name="registro"),
    path("iniciar_sesion/", iniciar_sesion, name="iniciar_sesion"),
    path("cerrar_sesion/", cerrar_sesion, name="cerrar_sesion"),
    path('perfil/', perfil_usuario, name='perfil_usuario'),
    path('registro/', registro, name='registro'),
]
