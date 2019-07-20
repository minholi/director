from django.db import models

class Situacao(models.Model):
    id = models.IntegerField(primary_key=True)
    situacao = models.CharField(max_length=40, verbose_name='situação')
    descricao = models.TextField(blank=True, verbose_name='descrição')
    conversivel = models.BooleanField(verbose_name='conversível', default=False)
    conversao = models.ForeignKey('self', on_delete=models.PROTECT, verbose_name='conversão', null=True, blank=True)

    def __str__(self):
        return self.situacaos

    class Meta:
        abstract = True

class Cadastral(Situacao):
    class Meta:
        verbose_name = 'sit. cadastral'
        verbose_name_plural = "sit. cadastrais"

class Origem(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Lead(models.Model):
    nome = models.CharField(max_length=255)
    origem = models.ForeignKey(Origem, on_delete=models.PROTECT)
    cadastral = models.ForeignKey(Cadastral, on_delete=models.PROTECT, verbose_name='situação')

    def __str__(self):
        return '%s - %s' % (self.nome, self.origem)

