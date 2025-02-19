from django.urls import path
from .views import index  # Certifique-se de que a função index já está no views.py

urlpatterns = [
    path("", index, name="index"),  # Página inicial em "/"
    path("partidas/", index, name="partidas"),  # Página acessível via "/partidas/"
]
