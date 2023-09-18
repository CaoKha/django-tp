from dotenv import load_dotenv
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env/dev/.env.django.dev")

wsgi_app = "django_app.wsgi"
bind = f"0.0.0.0:{os.environ.get('DJANGO_PORT')}"
