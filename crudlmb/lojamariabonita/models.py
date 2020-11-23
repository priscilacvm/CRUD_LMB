from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    telefone = models.CharField(max_length=14, blank=True, null=True)
    Endereco = models.CharField(max_length=100, blank=True, null=True)
    Bairro = models.CharField(max_length=50, blank=True, null=True)
    CEP = models.CharField(max_length=9, blank=True, null=True)
    Referencia = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.nome
