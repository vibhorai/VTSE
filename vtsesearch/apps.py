from django.apps import AppConfig


class VtsesearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vtsesearch'

    def ready(self):
        import vtsesearch.signals
