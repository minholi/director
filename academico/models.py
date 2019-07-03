from django.db import models
from base.models import Pessoa

class Presenca(models.Model):
    id = models.IntegerField(primary_key=True)
    situacao = models.CharField(max_length=40, verbose_name='situação')
    descricao = models.TextField(blank=True, verbose_name='descrição')

    def __str__(self):
        return self.situacao

    class Meta:
        verbose_name = "sit. de presença"
        verbose_name_plural = verbose_name

class Desempenho(models.Model):
    id = models.IntegerField(primary_key=True)
    situacao = models.CharField(max_length=40, verbose_name='situação')
    descricao = models.TextField(blank=True, verbose_name='descrição')

    def __str__(self):
        return self.situacao

    class Meta:
        verbose_name = "sit. de desempenho"
        verbose_name_plural = verbose_name

class Financeiro(models.Model):
    id = models.IntegerField(primary_key=True)
    situacao = models.CharField(max_length=40, verbose_name='situação')
    descricao = models.TextField(blank=True, verbose_name='descrição')
    reversivel = models.BooleanField(verbose_name='reversível', default=False)
    reversao = models.ForeignKey('Financeiro', on_delete=models.PROTECT, verbose_name='reversão', null=True, blank=True)

    def __str__(self):
        return self.situacao

    class Meta:
        verbose_name = "sit. financeira"
        verbose_name_plural = "sit. financeiras"

class Matricula(models.Model):
    id = models.IntegerField(primary_key=True)
    situacao = models.CharField(max_length=40, verbose_name='situação')
    descricao = models.TextField(blank=True, verbose_name='descrição')

    def __str__(self):
        return self.situacao

    class Meta:
        verbose_name = "sit. de matrícula"
        verbose_name_plural = verbose_name

class Documentacao(models.Model):
    id = models.IntegerField(primary_key=True)
    situacao = models.CharField(max_length=40, verbose_name='situação')
    descricao = models.TextField(blank=True, verbose_name='descrição')

    def __str__(self):
        return self.situacao

    class Meta:
        verbose_name = "sit. de documentação"
        verbose_name_plural = verbose_name

class Andamento(models.Model):
    id = models.IntegerField(primary_key=True)
    situacao = models.CharField(max_length=40, verbose_name='situação')
    descricao = models.TextField(blank=True, verbose_name='descrição')

    def __str__(self):
        return self.situacao

    class Meta:
        verbose_name = "sit. de andamento"
        verbose_name_plural = verbose_name

class Situacao(models.Model):
    id = models.IntegerField(primary_key=True)
    situacao = models.CharField(max_length=40, verbose_name='situação')
    descricao = models.TextField(blank=True, verbose_name='descrição')

    def __str__(self):
        return self.situacao

    class Meta:
        verbose_name = "sit. cadastral"
        verbose_name_plural = "sit. cadastrais"

class Aluno(models.Model):
    ra = models.CharField(max_length=20, verbose_name='RA')
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    curso = models.CharField(max_length=255)
    curriculo = models.CharField(max_length=40, verbose_name='currículo')
    serie = models.IntegerField(verbose_name='série')
    polo = models.CharField(max_length=255)
    presenca = models.ForeignKey(Presenca, on_delete=models.PROTECT, verbose_name='presença')
    desempenho = models.ForeignKey(Desempenho, on_delete=models.PROTECT)
    financeiro = models.ForeignKey(Financeiro, on_delete=models.PROTECT)
    matricula = models.ForeignKey(Matricula, on_delete=models.PROTECT, verbose_name='matrícula')
    documentacao = models.ForeignKey(Documentacao, on_delete=models.PROTECT, verbose_name='documentação')
    andamento = models.ForeignKey(Andamento, on_delete=models.PROTECT)
    situacao = models.ForeignKey(Situacao, on_delete=models.PROTECT, verbose_name='situação')

    def __str__(self):
        return self.ra
