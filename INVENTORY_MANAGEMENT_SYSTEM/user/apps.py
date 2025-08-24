from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
# This ensures the auto profile creation signal works
def ready(self):
    from user import signals