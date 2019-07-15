from django.db import models
from academico.models import Aluno

# TODO: Vincular situações com tipos de ações
# isso permitirá relacionar ações e conversões
class TipoAcao(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, verbose_name='descrição')
    alunos = models.BooleanField(default=False)
    candidatos = models.BooleanField(default=False)
    leads = models.BooleanField(default=False)

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

class AcaoAlunoManager(models.Manager):
    def get_queryset(self):
        return super(AcaoAlunoManager, self).get_queryset().filter(
            alunos=True)

class AcaoAluno(TipoAcao):
    objects = AcaoAlunoManager()
    class Meta:
        proxy = True



class Atendimento(models.Model):
    data = models.DateTimeField()
    obs = models.TextField(blank=True)

    class Meta:
        abstract = True


class AtendimentoAluno(Atendimento):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    acao = models.ForeignKey(AcaoAluno, on_delete=models.CASCADE)

    def __str__(self):
        '%s - %s - %s' % (self.aluno, self.acao, self.data)

    class Meta:
        verbose_name = 'atendimento'