# apostas_app/views.py

from django.shortcuts import render
from .models import Partida

def partidas_publicas(request):
    partidas = Partida.objects.all()



    return render(request, 'index.html', {'partidas': partidas})


