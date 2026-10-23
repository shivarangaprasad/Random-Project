from django.urls import path

from random_console.views import home


urlpatterns = [
    path("", home, name="home"),
]
