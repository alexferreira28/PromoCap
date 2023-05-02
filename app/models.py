from django.db import models

# Create your models here.
class user(models.Model):
    nome = models.CharField(max_length=150)
    cnpj= models.CharField (max_length=18)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=20)

class prod(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    valor = models.FloatField(max_length=20)
