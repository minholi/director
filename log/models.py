from django.db import models
from academico.models import Aluno, Presenca, Nota, Financeira, Matricula, Documentacao, Andamento, Cadastral
from django.db.models import signals
from django.dispatch import receiver
from django.utils import timezone


class LogAluno(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data = models.DateField(db_index=True)
    hora = models.TimeField()

    class Meta:
        abstract = True
        unique_together = ['aluno', 'data', 'hora']

class TransAlunoPresenca(LogAluno):
    anterior = models.ForeignKey(Presenca, on_delete=models.CASCADE, related_name='presenca_anterior', blank=True, null=True)
    situacao = models.ForeignKey(Presenca, on_delete=models.CASCADE)

    def __str__(self):
        sit_anterior = self.anterior if self.anterior else 'Nada'
        return '[%s] %s - %s > %s' % (self.data, self.aluno, sit_anterior, self.situacao)

class TransAlunoNota(LogAluno):
    anterior = models.ForeignKey(Nota, on_delete=models.CASCADE, related_name='nota_anterior', blank=True, null=True)
    situacao = models.ForeignKey(Nota, on_delete=models.CASCADE)

    def __str__(self):
        sit_anterior = self.anterior if self.anterior else 'Nada'
        return '[%s] %s - %s > %s' % (self.data, self.aluno, sit_anterior, self.situacao)

class TransAlunoFinanceira(LogAluno):
    anterior = models.ForeignKey(Financeira, on_delete=models.CASCADE, related_name='financeira_anterior', blank=True, null=True)
    situacao = models.ForeignKey(Financeira, on_delete=models.CASCADE)

    def __str__(self):
        sit_anterior = self.anterior if self.anterior else 'Nada'
        return '[%s] %s - %s > %s' % (self.data, self.aluno, sit_anterior, self.situacao)

class TransAlunoMatricula(LogAluno):
    anterior = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name='matricula_anterior', blank=True, null=True)
    situacao = models.ForeignKey(Matricula, on_delete=models.CASCADE)

    def __str__(self):
        sit_anterior = self.anterior if self.anterior else 'Nada'
        return '[%s] %s - %s > %s' % (self.data, self.aluno, sit_anterior, self.situacao)

class TempoAluno(LogAluno):
    presenca = models.ForeignKey(Presenca, on_delete=models.CASCADE, verbose_name='presença')
    nota = models.ForeignKey(Nota, on_delete=models.CASCADE)
    financeira = models.ForeignKey(Financeira, on_delete=models.CASCADE)
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, verbose_name='matrícula')
    documentacao = models.ForeignKey(Documentacao, on_delete=models.CASCADE, verbose_name='documentação')
    andamento = models.ForeignKey(Andamento, on_delete=models.CASCADE)
    cadastral = models.ForeignKey(Cadastral, on_delete=models.CASCADE, verbose_name='situação')

    def __str__(self):
        return '[%s] %s - %s' % (self.data, self.aluno, self.situacao)

@receiver(signals.pre_save, sender=Aluno)
def log_trans_aluno(sender, instance, **kwargs):
    now = timezone.now()
    try:
        anterior = Aluno.objects.get(pk=instance)
        presenca_anterior = anterior.presenca
        nota_anterior = anterior.nota
        financeira_anterior = anterior.financeira
        matricula_anterior = anterior.matricula
    except Aluno.DoesNotExist:
        presenca_anterior = None
        nota_anterior = None
        financeira_anterior = None
        matricula_anterior = None

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
