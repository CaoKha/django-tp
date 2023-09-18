import os
from pathlib import Path
import dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

dotenv.load_dotenv(BASE_DIR / ".env/dev/.env.django.dev")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "+s@j=(0awsa!md#i_y64!cuz9v)^f4blbh!w0d+y2*0p+eazw$"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["backend", "localhost", "127.0.0.1"]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "rest_framework",
    "corsheaders",
    # app
    "messages_api",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_app.middleware.Auth0Middleware",
    # "csp.middleware.CSPMiddleware",
]

ROOT_URLCONF = "django_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_app.wsgi.application"

# Database

# Github actions database
if os.environ.get("EXTERNAL_DATABASE"):
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
# SQLite database if not using Docker for development
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Warsaw"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Django REST Framework config
# https://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTTokenUserAuthentication"
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# required by django.contrib.sites
SITE_ID = 1


# CORS
CORS_ALLOW_ALL_ORIGINS = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 31536000
# CSP_FRAME_ANCESTORS = "'none'"
# CSP_DEFAULT_SRC = ("'none'",)
# CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com')
# CSP_SCRIPT_SRC = ("'self'",)
# CSP_FONT_SRC = ("'self'", 'fonts.gstatic.com')
# CSP_IMG_SRC = ("'self'",)

# JWT
AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN", "kha-dev.eu.auth0.com")
AUTH0_AUDIENCE = os.environ.get("AUTH0_AUDIENCE", "https://tp-django.example.com")
SIMPLE_JWT = {
    "ALGORITHM": "RS256",
    "JWK_URL": f"https://{AUTH0_DOMAIN}/.well-known/jwks.json",
    "AUDIENCE": AUTH0_AUDIENCE,
    "ISSUER": f"https://{AUTH0_DOMAIN}/",
    "USER_ID_CLAIM": "sub",
    "AUTH_TOKEN_CLASSES": ("auth.tokens.Auth0Token",),
}
