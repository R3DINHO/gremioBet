from django.shortcuts import render
from django.utils.timezone import now
from .models import Partida

def index(request):
    # Obtém todas as partidas futuras ordenadas pela data mais próxima
    partidas = Partida.objects.filter(data__gte=now()).order_by('data')

    return render(request, "apostas/index.html", {"partidas": partidas})
