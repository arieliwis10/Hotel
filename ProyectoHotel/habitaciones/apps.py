from django.apps import AppConfig


class HabitacionesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'habitaciones'
    
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import usuarios.signals
