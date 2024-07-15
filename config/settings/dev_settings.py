import os
from .base_settings import *

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = bool(int(os.environ.get("DEBUG", default=0)))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(",")

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DB_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("DB_USER", "user"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "password"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": int(os.environ.get("DB_PORT", 5432)),
    }
}

CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(",")

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')