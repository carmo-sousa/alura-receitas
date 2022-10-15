from django.db import models


class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_receita


class Classe(models.Model):
    nome = models.CharField(max_length=100)
