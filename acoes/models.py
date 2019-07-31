from django.db import models

# TODO: Vincular situações com tipos de ações
# isso permitirá relacionar ações e conversões
class TipoAcao(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, verbose_name='descrição')
    alunos = models.BooleanField(default=False)
    inscritos = models.BooleanField(default=False)
    contatos = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'tipo de ação'
        verbose_name_plural = 'tipos de ações'


class Acao(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, verbose_name='descrição')
    tipo = models.ForeignKey(TipoAcao, on_delete=models.PROTECT)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'ação'
        verbose_name_plural = 'ações'


class Atendimento(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    obs = models.TextField(blank=True)

    class Meta:
        abstract = True


class AtendimentoAgendado(models.Model):
    data = models.DateTimeField()
    realizado = models.DateTimeField(null=True, blank=True)
    exito = models.BooleanField(default=False, verbose_name='êxito')

    class Meta:
        abstract = True

