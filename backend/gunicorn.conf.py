from dotenv import load_dotenv
from common.utils import get_env_var
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env/dev/.env.django.dev")

wsgi_app = "django_app.wsgi"
bind = f"0.0.0.0:{get_env_var('DJANGO_PORT')}"
