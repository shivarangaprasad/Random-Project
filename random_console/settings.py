import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-only-change-me")
DEBUG = os.environ.get("DJANGO_DEBUG", "true").lower() == "true"
ALLOWED_HOSTS = os.environ.get(
    "DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost"
).split(",")
ROOT_URLCONF = "random_console.urls"
INSTALLED_APPS = ["random_console"]
MIDDLEWARE = []
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": False,
        "OPTIONS": {},
    },
]
WSGI_APPLICATION = "random_console.wsgi.application"
