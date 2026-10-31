from random import randint

from django.shortcuts import render


def home(request):
    number = randint(1, 10000)
    color = f"#{randint(0, 0xFFFFFF):06X}"
    return render(request, "index.html", {"number": number, "color": color})
