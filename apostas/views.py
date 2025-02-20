# apostas/views.py
from django.shortcuts import render
from .models import Partida  # Certifique-se de que o modelo está importado

def index(request):
    partidas = Partida.objects.order_by('data') # Busca todas as partidas no banco
    return render(request, "apostas/index.html", {"partidas": partidas})
