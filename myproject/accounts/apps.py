from django.apps import AppConfig

# import sys
# from pathlib import Path

# sys.path.append(str(Path("..").resolve()))


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self):
        from . import signals
