from django.db import models
import acoes.models as ma
from ingresso.models import Inscrito
from taggit.managers import TaggableManager

class Situacao(models.Model):
    id = models.IntegerField(primary_key=True)
    situacao = models.CharField(max_length=40, verbose_name='situação')
    descricao = models.TextField(blank=True, verbose_name='descrição')
    conversivel = models.BooleanField(verbose_name='conversível', default=False)
    conversao = models.ForeignKey('self', on_delete=models.PROTECT, verbose_name='conversão', null=True, blank=True)

    def __str__(self):
        return self.situacao

    class Meta:
        abstract = True

class Cadastral(Situacao):
    class Meta:
        verbose_name = 'sit. cadastral'
        verbose_name_plural = "sit. cadastrais"

class Status(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, verbose_name='descrição')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'status'

class Origem(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, verbose_name='descrição')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'origens'

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    site = models.URLField(blank=True, null=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    pais = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    obs = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, blank=True, null=True)
    nao_ligar = models.BooleanField(default=False, verbose_name='não ligar')
    # TODO: Registrar log de atendimentos marcados e desmarcar automaticamente após 10 minutos
    em_atendimento = models.BooleanField(default=False, verbose_name='em atendimento')
    origem = models.ForeignKey(Origem, on_delete=models.PROTECT)
    cadastral = models.ForeignKey(Cadastral, on_delete=models.PROTECT, verbose_name='situação')
    criacao = models.DateTimeField(auto_now_add=True, verbose_name='criação')
    atualizacao = models.DateTimeField(auto_now=True, verbose_name='atualização')
    inscricoes = models.ManyToManyField(Inscrito, through='Conversao')

    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.nome

    # TODO: Usar o annotate pra transformar isso em algo que possa ser usado para ordenar a listagem e melhorar a performance
    def proximo_atendimento_agendado(self):
        paa = self.atendimentoagendado_set.filter(realizado__isnull=True).order_by('data').first()
        return paa.data
    proximo_atendimento_agendado.short_description = 'próx. atend. agendado'    


class AcaoManager(models.Manager):
    def get_queryset(self):
        return super(AcaoManager, self).get_queryset().filter(
            tipo__contatos=True)

class Acao(ma.Acao):
    objects = AcaoManager()
    class Meta:
        proxy = True
        verbose_name = 'ação'
        verbose_name_plural = 'ações'


class Atendimento(ma.Atendimento):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    acao = models.ForeignKey(Acao, on_delete=models.PROTECT, related_name='atendimentos', verbose_name='ação')

    def __str__(self):
        return '%s - %s - %s' % (self.contato, self.acao, self.data)

    class Meta:
        verbose_name = 'atendimento'


class AtendimentoAgendado(ma.AtendimentoAgendado):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    acao = models.ForeignKey(Acao, on_delete=models.PROTECT, related_name='atendimentos_agendados', verbose_name='ação')

    def __str__(self):
        return '%s - %s - %s' % (self.contato, self.acao, self.data)

    class Meta:
        verbose_name_plural = 'atendimentos agendados'


class Conversao(models.Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    inscrito = models.ForeignKey(Inscrito, on_delete=models.CASCADE)
    acao = models.ForeignKey(Acao, on_delete=models.PROTECT, verbose_name='ação')
    data = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s - %s' % (self.inscrito, self.acao, self.data)

    class Meta:
        verbose_name = 'conversão'
        verbose_name_plural = 'conversões'
