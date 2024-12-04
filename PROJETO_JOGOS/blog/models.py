from django.conf import settings
from django.db import models

class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    duracao = models.CharField(max_length=20)

