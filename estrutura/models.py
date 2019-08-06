from django.db import models
from django.contrib.auth.models import AbstractUser

class Setor(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, verbose_name='descrição')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'setores'


class Unidade(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, verbose_name='descrição')

    def __str__(self):
        return self.nome


class Usuario(AbstractUser):
    setor = models.ForeignKey(Setor, null=True, blank=True, on_delete=models.PROTECT)
    unidade = models.ForeignKey(Unidade, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return '%s (%s - %s)' % (self.first_name, self.setor, self.unidade)