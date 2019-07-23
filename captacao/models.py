from django.db import models
import acoes.models as ma

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

class Lead(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    celular = models.CharField(max_length=15, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    naoligar = models.BooleanField(default=False, verbose_name='não ligar')
    origem = models.ForeignKey(Origem, on_delete=models.PROTECT)
    cadastral = models.ForeignKey(Cadastral, on_delete=models.PROTECT, verbose_name='situação')
    criacao = models.DateTimeField(auto_now_add=True, verbose_name='criação')
    atualizacao = models.DateTimeField(auto_now=True, verbose_name='atualização')

    def __str__(self):
        return '%s - %s' % (self.nome, self.origem)

class AcaoManager(models.Manager):
    def get_queryset(self):
        return super(AcaoManager, self).get_queryset().filter(
            tipo__leads=True)

class Acao(ma.Acao):
    objects = AcaoManager()
    class Meta:
        proxy = True


class Atendimento(ma.Atendimento):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE, related_name='leads')

    def __str__(self):
        return '%s - %s - %s' % (self.lead, self.acao, self.data)

    class Meta:
        verbose_name = 'atendimento'