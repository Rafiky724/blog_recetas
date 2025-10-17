from django.apps import AppConfig

class RecetasAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recetas_app'
    
    def ready(self):
        import recetas_app.signals