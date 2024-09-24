from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import habitaciones, consultar_reserva
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path("habitaciones/", habitaciones, name="habitaciones"),
    path('consulta/', consultar_reserva, name='consultar_reserva'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)