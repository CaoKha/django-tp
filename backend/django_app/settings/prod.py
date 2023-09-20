"""
Configuration for development with Docker.
"""
import os

from django_app.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "production")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["backend", "localhost", "127.0.0.1", "0.0.0.0"]

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("SQL_DATABASE_NAME", "postgres"),
        "USER": os.environ.get("SQL_USER", "postgres"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "postgres"),
        "HOST": os.environ.get("SQL_HOST", "db"),  # set in docker-compose.yml
        "PORT": os.environ.get("SQL_PORT", "5432"),  # default postgres port
    }
}

INSTALLED_APPS.append("django_vite")

# project directory
ROOT_DIR = BASE_DIR.parent

# whitenoise middleware - has to be first in the list
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# extra directories with html files
TEMPLATES[0]["DIRS"] = [
    # os.path.join(ROOT_DIR, "frontend", "dist"),
    BASE_DIR / "templates",
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Where ViteJS assets are built.
DJANGO_VITE_ASSETS_PATH = ROOT_DIR / "frontend" / "dist"

# If use HMR or not.
DJANGO_VITE_DEV_MODE = DEBUG

# Name of static files folder (after called python manage.py collectstatic)
STATIC_ROOT = BASE_DIR / "static"

# Include DJANGO_VITE_ASSETS_PATH into STATICFILES_DIRS to be copied inside
# when run command python manage.py collectstatic
STATICFILES_DIRS = [DJANGO_VITE_ASSETS_PATH]
