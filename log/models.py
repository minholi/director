from django.db import models
import relacionamento.models as rel
import ingresso.models as ing
import captacao.models as cap
from django.db.models import signals
from django.dispatch import receiver
from django.utils import timezone


class LogContato(models.Model):
    contato = models.ForeignKey(cap.Contato, on_delete=models.CASCADE)
    data = models.DateField(db_index=True)
    hora = models.TimeField()

    class Meta:
        abstract = True
        unique_together = ['contato', 'data', 'hora']

class TransContatoCadastral(LogContato):
    anterior = models.ForeignKey(cap.SitCadastral, on_delete=models.CASCADE, related_name='cadastral_anterior', blank=True, null=True)
    situacao = models.ForeignKey(cap.SitCadastral, on_delete=models.CASCADE)

    def __str__(self):
        sit_anterior = self.anterior if self.anterior else 'Nada'
        return '[%s] %s - %s > %s' % (self.data, self.contato, sit_anterior, self.situacao)


class TempoContato(LogContato):
    cadastral = models.ForeignKey(rel.SitCadastral, on_delete=models.CASCADE, verbose_name='situação')

    def __str__(self):
        return '[%s] %s - %s' % (self.data, self.contato, self.situacao)

@receiver(signals.pre_save, sender=cap.Contato)
def log_trans_contato(sender, instance, **kwargs):
    now = timezone.now()
    try:
        anterior = cap.Contato.objects.get(pk=instance)
        cadastral_anterior = anterior.cadastral
    except cap.Contato.DoesNotExist:
        cadastral_anterior = None

    if instance.cadastral != cadastral_anterior:
        print('%s: %s > %s' % (instance, cadastral_anterior, instance.cadastral)) 
        log = TransContatoCadastral(contato=instance, data=now.date(), hora=now.time(), anterior=cadastral_anterior, situacao=instance.cadastral)
        log.save()



class LogInscrito(models.Model):
    inscrito = models.ForeignKey(ing.Inscrito, on_delete=models.CASCADE)
    data = models.DateField(db_index=True)
    hora = models.TimeField()

    class Meta:
        abstract = True
        unique_together = ['inscrito', 'data', 'hora']

class TransInscritoCadastral(LogInscrito):
    anterior = models.ForeignKey(ing.SitCadastral, on_delete=models.CASCADE, related_name='cadastral_anterior', blank=True, null=True)
    situacao = models.ForeignKey(ing.SitCadastral, on_delete=models.CASCADE)

    def __str__(self):
        sit_anterior = self.anterior if self.anterior else 'Nada'
        return '[%s] %s - %s > %s' % (self.data, self.inscrito, sit_anterior, self.situacao)


class TempoInscrito(LogInscrito):
    cadastral = models.ForeignKey(rel.SitCadastral, on_delete=models.CASCADE, verbose_name='situação')

    def __str__(self):
        return '[%s] %s - %s' % (self.data, self.inscrito, self.situacao)

@receiver(signals.pre_save, sender=ing.Inscrito)
def log_trans_inscrito(sender, instance, **kwargs):
    now = timezone.now()
    try:
        anterior = ing.Inscrito.objects.get(pk=instance)
        cadastral_anterior = anterior.cadastral
    except ing.Inscrito.DoesNotExist:
        cadastral_anterior = None

    if instance.cadastral != cadastral_anterior:
        print('%s: %s > %s' % (instance, cadastral_anterior, instance.cadastral)) 
        log = TransInscritoCadastral(inscrito=instance, data=now.date(), hora=now.time(), anterior=cadastral_anterior, situacao=instance.cadastral)
        log.save()


class LogAluno(models.Model):
    aluno = models.ForeignKey(rel.Aluno, on_delete=models.CASCADE)
    data = models.DateField(db_index=True)
    hora = models.TimeField()

    class Meta:
        abstract = True
        unique_together = ['aluno', 'data', 'hora']

class TransAlunoPresenca(LogAluno):
    anterior = models.ForeignKey(rel.SitPresenca, on_delete=models.CASCADE, related_name='presenca_anterior', blank=True, null=True)
    situacao = models.ForeignKey(rel.SitPresenca, on_delete=models.CASCADE)

    def __str__(self):
        sit_anterior = self.anterior if self.anterior else 'Nada'
        return '[%s] %s - %s > %s' % (self.data, self.aluno, sit_anterior, self.situacao)

class TransAlunoNota(LogAluno):
    anterior = models.ForeignKey(rel.SitNota, on_delete=models.CASCADE, related_name='nota_anterior', blank=True, null=True)
    situacao = models.ForeignKey(rel.SitNota, on_delete=models.CASCADE)

    def __str__(self):
        sit_anterior = self.anterior if self.anterior else 'Nada'
        return '[%s] %s - %s > %s' % (self.data, self.aluno, sit_anterior, self.situacao)

class TransAlunoFinanceira(LogAluno):
    anterior = models.ForeignKey(rel.SitFinanceira, on_delete=models.CASCADE, related_name='financeira_anterior', blank=True, null=True)
    situacao = models.ForeignKey(rel.SitFinanceira, on_delete=models.CASCADE)

    def __str__(self):
        sit_anterior = self.anterior if self.anterior else 'Nada'
        return '[%s] %s - %s > %s' % (self.data, self.aluno, sit_anterior, self.situacao)

class TransAlunoMatricula(LogAluno):
    anterior = models.ForeignKey(rel.SitMatricula, on_delete=models.CASCADE, related_name='matricula_anterior', blank=True, null=True)
    situacao = models.ForeignKey(rel.SitMatricula, on_delete=models.CASCADE)

    def __str__(self):
        sit_anterior = self.anterior if self.anterior else 'Nada'
        return '[%s] %s - %s > %s' % (self.data, self.aluno, sit_anterior, self.situacao)

class TransAlunoDocumentacao(LogAluno):
    anterior = models.ForeignKey(rel.SitDocumentacao, on_delete=models.CASCADE, related_name='documentacao_anterior', blank=True, null=True)
    situacao = models.ForeignKey(rel.SitDocumentacao, on_delete=models.CASCADE)

    def __str__(self):
        sit_anterior = self.anterior if self.anterior else 'Nada'
        return '[%s] %s - %s > %s' % (self.data, self.aluno, sit_anterior, self.situacao)

class TransAlunoAndamento(LogAluno):
    anterior = models.ForeignKey(rel.SitAndamento, on_delete=models.CASCADE, related_name='andamento_anterior', blank=True, null=True)
    situacao = models.ForeignKey(rel.SitAndamento, on_delete=models.CASCADE)

    def __str__(self):
        sit_anterior = self.anterior if self.anterior else 'Nada'
        return '[%s] %s - %s > %s' % (self.data, self.aluno, sit_anterior, self.situacao)

class TransAlunoCadastral(LogAluno):
    anterior = models.ForeignKey(rel.SitCadastral, on_delete=models.CASCADE, related_name='cadastral_anterior', blank=True, null=True)
    situacao = models.ForeignKey(rel.SitCadastral, on_delete=models.CASCADE)

    def __str__(self):
        sit_anterior = self.anterior if self.anterior else 'Nada'
        return '[%s] %s - %s > %s' % (self.data, self.aluno, sit_anterior, self.situacao)

class TempoAluno(LogAluno):
    presenca = models.ForeignKey(rel.SitPresenca, on_delete=models.CASCADE, verbose_name='presença')
    nota = models.ForeignKey(rel.SitNota, on_delete=models.CASCADE)
    financeira = models.ForeignKey(rel.SitFinanceira, on_delete=models.CASCADE)
    matricula = models.ForeignKey(rel.SitMatricula, on_delete=models.CASCADE, verbose_name='matrícula')
    documentacao = models.ForeignKey(rel.SitDocumentacao, on_delete=models.CASCADE, verbose_name='documentação')
    andamento = models.ForeignKey(rel.SitAndamento, on_delete=models.CASCADE)
    cadastral = models.ForeignKey(rel.SitCadastral, on_delete=models.CASCADE, verbose_name='situação')

    def __str__(self):
        return '[%s] %s - %s' % (self.data, self.aluno, self.situacao)

@receiver(signals.pre_save, sender=rel.Aluno)
def log_trans_aluno(sender, instance, **kwargs):
    now = timezone.now()
    try:
        anterior = rel.Aluno.objects.get(pk=instance)
        presenca_anterior = anterior.presenca
        nota_anterior = anterior.nota
        financeira_anterior = anterior.financeira
        matricula_anterior = anterior.matricula
        documentacao_anterior = anterior.documentacao
        andamento_anterior = anterior.andamento
        cadastral_anterior = anterior.cadastral
    except rel.Aluno.DoesNotExist:
        presenca_anterior = None
        nota_anterior = None
        financeira_anterior = None
        matricula_anterior = None
        documentacao_anterior = None
        andamento_anterior = None
        cadastral_anterior = None

    if instance.presenca != presenca_anterior:
        print('%s: %s > %s' % (instance, presenca_anterior, instance.presenca)) 
        # TransAlunoPresenca.objects.update_or_create(aluno=instance, data=now.date(), hora=now.time(), defaults={'anterior':presenca_anterior, 'situacao':instance.presenca})
        log = TransAlunoPresenca(aluno=instance, data=now.date(), hora=now.time(), anterior=presenca_anterior, situacao=instance.presenca)
        log.save()

    if instance.nota != nota_anterior:
        print('%s: %s > %s' % (instance, nota_anterior, instance.nota)) 
        log = TransAlunoNota(aluno=instance, data=now.date(), hora=now.time(), anterior=nota_anterior, situacao=instance.nota)
        log.save()

    if instance.financeira != financeira_anterior:
        print('%s: %s > %s' % (instance, financeira_anterior, instance.financeira)) 
        log = TransAlunoFinanceira(aluno=instance, data=now.date(), hora=now.time(), anterior=financeira_anterior, situacao=instance.financeira)
        log.save()

    if instance.matricula != matricula_anterior:
        print('%s: %s > %s' % (instance, matricula_anterior, instance.matricula)) 
        log = TransAlunoMatricula(aluno=instance, data=now.date(), hora=now.time(), anterior=matricula_anterior, situacao=instance.matricula)
        log.save()

    if instance.documentacao != documentacao_anterior:
        print('%s: %s > %s' % (instance, documentacao_anterior, instance.documentacao)) 
        log = TransAlunoDocumentacao(aluno=instance, data=now.date(), hora=now.time(), anterior=documentacao_anterior, situacao=instance.documentacao)
        log.save()

    if instance.andamento != andamento_anterior:
        print('%s: %s > %s' % (instance, andamento_anterior, instance.andamento)) 
        log = TransAlunoAndamento(aluno=instance, data=now.date(), hora=now.time(), anterior=andamento_anterior, situacao=instance.andamento)
        log.save()

    if instance.cadastral != cadastral_anterior:
        print('%s: %s > %s' % (instance, cadastral_anterior, instance.cadastral)) 
        log = TransAlunoCadastral(aluno=instance, data=now.date(), hora=now.time(), anterior=cadastral_anterior, situacao=instance.cadastral)
        log.save()