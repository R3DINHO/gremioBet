from django.shortcuts import render
from .models import Partida  # Certifique-se de que o modelo está importado

def index(request):
    partidas = Partida.objects.all()  # Busca todas as partidas no banco
    return render(request, "index.html", {"partidas": partidas})
