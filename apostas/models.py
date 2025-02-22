from django.db import models

class Partida(models.Model):
    opcoes = [("fem", "feminino"), ("masc", "masculino")]
    modalidade = models.CharField(max_length=4, choices=opcoes)
    time_casa = models.CharField(max_length=100)
    time_fora = models.CharField(max_length=100)
    data = models.DateTimeField()
    odds_casa = models.FloatField()
    odds_fora = models.FloatField()
    odds_empate = models.FloatField()
    ambasMarcamSim = models.FloatField(default=0.0)
    ambasMarcamNao = models.FloatField(default=0.0)
    maisGols = models.FloatField(default=0.0)
    menosGols = models.FloatField(default=0.0)
    cor_casa = models.CharField(max_length=7, default="#000000")
    cor_fora = models.CharField(max_length=7, default="#000000")

    def __str__(self):
        return f'{self.time_casa} vs {self.time_fora} - {self.data}'

# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_image = models.CharField(max_length=255, default="img/fotosPerfil/default.png")
    gremio_coins = models.IntegerField(default=100)

    # Função para retornar a URL da imagem de perfil
    def get_imagem_perfil_url(self):
        
        return f"/static/{self.profile_image}" 


    gremio_coins = models.IntegerField(default=100)