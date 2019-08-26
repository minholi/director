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

class SitCadastral(Situacao):
    class Meta:
        verbose_name = "sit. cadastral"
        verbose_name_plural = "sit. cadastrais"

class Status(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, verbose_name='descrição')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'status'

class Inscrito(models.Model):
    codigo = models.CharField(max_length=20, verbose_name='código', primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    concurso = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    polo = models.CharField(max_length=255)
    ano = models.CharField(max_length=4)
    periodo = models.CharField(max_length=2)
    cadastral = models.ForeignKey(SitCadastral, on_delete=models.PROTECT, verbose_name='situação')
    obs = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, blank=True, null=True)
    criacao = models.DateTimeField(auto_now_add=True, verbose_name='criação')
    atualizacao = models.DateTimeField(auto_now=True, verbose_name='atualização')

    def __str__(self):
        return '%s - %s' % (self.codigo, self.nome)


class AcaoManager(models.Manager):
    def get_queryset(self):
        return super(AcaoManager, self).get_queryset().filter(
            tipo__inscritos=True)

class Acao(ma.Acao):
    objects = AcaoManager()
    class Meta:
        proxy = True
        verbose_name = 'ação'
        verbose_name_plural = 'ações'

class Atendimento(ma.Atendimento):
    inscrito = models.ForeignKey(Inscrito, on_delete=models.CASCADE)
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE, verbose_name='ação')

    def __str__(self):
        return '%s - %s - %s' % (self.inscrito, self.acao, self.data)

    class Meta:
        verbose_name = 'atendimento'
        default_related_name = 'inscritos'