from django.db import models
from relacionamento import models as rel_models

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

class Presenca(Situacao):
    class Meta:
        verbose_name = "presença"

class Nota(Situacao):
    pass

class Atividade(Situacao):
    pass

class Financeira(Situacao):
    pass

class Matricula(Situacao):
    class Meta:
        verbose_name = "matrícula"

class Documentacao(Situacao):
    class Meta:
        verbose_name = "documentação"
        verbose_name_plural = verbose_name

class Andamento(Situacao):
    pass

class Cadastral(Situacao):
    class Meta:
        verbose_name_plural = "cadastrais"

class Aluno(models.Model):
    ra = models.CharField(max_length=20, verbose_name='RA', primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    curso = models.CharField(max_length=255)
    curriculo = models.CharField(max_length=40, verbose_name='currículo')
    serie = models.IntegerField(verbose_name='série')
    polo = models.CharField(max_length=255)
    presenca = models.ForeignKey(Presenca, on_delete=models.PROTECT, verbose_name='presença')
    nota = models.ForeignKey(Nota, on_delete=models.PROTECT)
    financeira = models.ForeignKey(Financeira, on_delete=models.PROTECT)
    matricula = models.ForeignKey(Matricula, on_delete=models.PROTECT, verbose_name='matrícula')
    documentacao = models.ForeignKey(Documentacao, on_delete=models.PROTECT, verbose_name='documentação')
    andamento = models.ForeignKey(Andamento, on_delete=models.PROTECT)
    cadastral = models.ForeignKey(Cadastral, on_delete=models.PROTECT, verbose_name='situação')

    def __str__(self):
        return self.ra


class AcaoManager(models.Manager):
    def get_queryset(self):
        return super(AcaoManager, self).get_queryset().filter(
            tipo__alunos=True)

class Acao(rel_models.Acao):
    objects = AcaoManager()
    class Meta:
        proxy = True

class Atendimento(rel_models.Atendimento):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s - %s' % (self.aluno, self.acao, self.data.strftime("%d-%m-%Y %H:%M"))

    class Meta:
        verbose_name = 'atendimento'