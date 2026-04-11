from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ALLOWED_HOSTS = ['staging.airportmanager.com', 'localhost']

# Seguridad adicional para staging
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False