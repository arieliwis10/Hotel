from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import habitaciones

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path("habitaciones/", habitaciones, name="habitaciones"),
]