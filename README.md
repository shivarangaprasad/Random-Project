# Django Random Number and Color

A small Django page that generates a random number from 1 to 100 and a random
hex color each time it is loaded.

## Run with Docker

Build the image from this folder (the repository root):

```sh
docker build -t django-random-console .
```

Run it locally:

```sh
docker run --rm -p 8000:8000 django-random-console
```

Open <http://127.0.0.1:8000/> and refresh to generate new values.

For a hosted container, configure `DJANGO_ALLOWED_HOSTS` to the hostname your
platform uses. For a private demo where the hostname is dynamic, `*` can be
used; a public deployment should set the specific hostname instead. Set
`DJANGO_SECRET_KEY` to a unique secret for any deployment.

The container listens on `PORT` when provided by the platform, or port 8000 by
default.

## Run without Docker

```sh
python -m pip install -r requirements.txt
python manage.py runserver
```

## Test

```sh
python manage.py test random_console
```
