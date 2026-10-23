FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_DEBUG=false

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN adduser --disabled-password --no-create-home appuser
USER appuser

EXPOSE 8000

CMD ["sh", "-c", "gunicorn --chdir /app --bind 0.0.0.0:${PORT:-8000} random_console.wsgi:application"]
