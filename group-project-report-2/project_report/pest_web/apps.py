from django.apps import AppConfig


class PestWebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pest_web'
class PestWebConfig(AppConfig):
    name = 'pest_web'

    def ready(self):
        import pest_web.signals