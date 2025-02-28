__version__ = "3.0.0"

try:
    import django

    if django.VERSION < (3, 2):
        default_app_config = "djmoney.apps.MoneyConfig"
except ModuleNotFoundError:
    # this part is useful for allow setup.py to be used for version checks
    pass

from . import baker_field_generator
