from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data_receita = models.DateTimeField(auto_now_add=True)
    foto_receita = models.ImageField(upload_to="fotos/%d/%m/%Y/", blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_receita

    class Meta:
        ordering = ["-data_receita"]
