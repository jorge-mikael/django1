from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField('nome',max_length=100)
    preco = models.DecimalField('preço', max_digits=10, decimal_places=2)
    estoque = models.IntegerField('Quantidade em estoque')

    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    nome = models.CharField('nome',max_length=100)
    sobrenome = models.CharField('sobrenome',max_length=100)
    email = models.EmailField('email',max_length=100)

    def __str__(self):
        return self.nome