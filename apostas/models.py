from django.db import models

class Partida(models.Model):
    idPartida = models.CharField()
    opcoes = [("fem", "feminino"), ("masc", "masculino")]
    modalidade = models.CharField(max_length=4, choices=opcoes)
    time_casa = models.CharField(max_length=100)
    time_fora = models.CharField(max_length=100)
    data = models.DateTimeField()
    odds_casa = models.IntegerField()
    odds_fora = models.IntegerField()
    odds_empate = models.IntegerField()
    ambasMarcamSim = models.IntegerField(default=0.0)
    ambasMarcamNao = models.IntegerField(default=0.0)
    maisGols = models.IntegerField(default=0.0)
    menosGols = models.IntegerField(default=0.0)
    cor_casa = models.CharField(max_length=7, default="#000000")
    cor_fora = models.CharField(max_length=7, default="#000000")

    def __str__(self):
        return f'{self.time_casa} vs {self.time_fora} - {self.data}'

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_image = models.CharField(max_length=255, default="default.png")
    gremio_coins = models.IntegerField(default=100)

    def get_imagem_perfil_url(self):
        if self.profile_image.startswith("img/fotosPerfil/"):
            return f"/static/{self.profile_image}"
        return f"/static/img/fotosPerfil/{self.profile_image}"



    gremio_coins = models.IntegerField(default=100)