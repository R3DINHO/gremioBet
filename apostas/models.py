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
