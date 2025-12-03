from django.apps import AppConfig


class OnlyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.only'
    verbose_name = "Основные настройки"