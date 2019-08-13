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

class SitPresenca(Situacao):
    class Meta:
        verbose_name = "presença"

class SitNota(Situacao):
    class Meta:
        verbose_name = 'nota'

class SitAtividade(Situacao):
    class Meta:
        verbose_name = 'atividade'

class SitFinanceira(Situacao):
    class Meta:
        verbose_name = 'finanaceira'

class SitMatricula(Situacao):
    class Meta:
        verbose_name = "matrícula"

class SitDocumentacao(Situacao):
    class Meta:
        verbose_name = "documentação"
        verbose_name_plural = verbose_name

class SitAndamento(Situacao):
    class Meta:
        verbose_name = "andamento"

class SitCadastral(Situacao):
    class Meta:
        verbose_name_plural = "cadastrais"

class Status(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, verbose_name='descrição')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'status'

class Aluno(models.Model):
    ra = models.CharField(max_length=20, verbose_name='RA', primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    curso = models.CharField(max_length=255)
    curriculo = models.CharField(max_length=40, verbose_name='currículo')
    serie = models.IntegerField(verbose_name='série')
    polo = models.CharField(max_length=255)
    presenca = models.ForeignKey(SitPresenca, on_delete=models.PROTECT, verbose_name='presença')
    nota = models.ForeignKey(SitNota, on_delete=models.PROTECT)
    financeira = models.ForeignKey(SitFinanceira, on_delete=models.PROTECT)
    matricula = models.ForeignKey(SitMatricula, on_delete=models.PROTECT, verbose_name='matrícula')
    documentacao = models.ForeignKey(SitDocumentacao, on_delete=models.PROTECT, verbose_name='documentação')
    andamento = models.ForeignKey(SitAndamento, on_delete=models.PROTECT)
    cadastral = models.ForeignKey(SitCadastral, on_delete=models.PROTECT, verbose_name='situação')
    obs = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, blank=True, null=True)
    criacao = models.DateTimeField(auto_now_add=True, verbose_name='criação')
    atualizacao = models.DateTimeField(auto_now=True, verbose_name='atualização')

    def __str__(self):
        return '%s - %s' % (self.ra, self.nome)


class Cobranca(models.Model):
    cobranca = models.IntegerField(unique=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20)
    ano = models.DecimalField(decimal_places=0, max_digits=4)
    mes = models.DecimalField(decimal_places=0, max_digits=2)
    data_venc = models.DateField(verbose_name='data de venc.')
    data_pgto = models.DateField(verbose_name='data de pgto.', null=True, blank=True)
    val_orig = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='val. orig.')
    val_final = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='val. final')
    val_pago = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True, verbose_name='val. pago')

    def __str__(self):
        return '%s' % self.cobranca


class Disciplina(models.Model):
    disciplina = models.IntegerField()
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    ano = models.DecimalField(decimal_places=0, max_digits=4)
    periodo = models.DecimalField(decimal_places=0, max_digits=2)
    serie = models.IntegerField(verbose_name='série')
    media = models.DecimalField(decimal_places=1, max_digits=3, verbose_name='média')
    media_min = models.DecimalField(decimal_places=1, max_digits=3, verbose_name='média min.')
    media_max = models.DecimalField(decimal_places=1, max_digits=3, verbose_name='média máx.')
    situacao = models.CharField(max_length=20)

    class Meta:
        unique_together = ['disciplina', 'aluno']

    def __str__(self):
        return '%s' % self.disciplina    


class Atividade(models.Model):
    disciplina = models.CharField(max_length=255)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    sigla = models.CharField(max_length=20)
    nome = models.CharField(max_length=255)
    ano = models.DecimalField(decimal_places=0, max_digits=4)
    periodo = models.DecimalField(decimal_places=0, max_digits=2)
    data_entrega = models.DateTimeField(verbose_name='data da entrega')
    nota = models.DecimalField(decimal_places=1, max_digits=3)
    nota_max = models.DecimalField(decimal_places=1, max_digits=3, verbose_name='nota máx.')

    class Meta:
        unique_together = ['disciplina', 'aluno', 'ano', 'periodo', 'sigla']

    def __str__(self):
        return '%s' % self.sigla



class AcaoManager(models.Manager):
    def get_queryset(self):
        return super(AcaoManager, self).get_queryset().filter(
            tipo__alunos=True)

class Acao(ma.Acao):
    objects = AcaoManager()
    class Meta:
        proxy = True


class Atendimento(ma.Atendimento):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s - %s' % (self.aluno, self.acao, self.data)

    class Meta:
        verbose_name = 'atendimento'
        default_related_name = 'alunos'