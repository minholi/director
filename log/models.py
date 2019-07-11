from django.db import models
from academico.models import Aluno, Presenca, Nota, Financeira, Matricula, Documentacao, Andamento, Cadastral
from django.db.models import signals
from django.dispatch import receiver


class Log(models.Model):
    data = models.DateTimeField(db_index=True)

    class Meta:
        abstract = True

class TransAlunoFinanceira(Log):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    anterior = models.ForeignKey(Financeira, on_delete=models.CASCADE, related_name='financeira_anterior')
    situacao = models.ForeignKey(Financeira, on_delete=models.CASCADE)

    def __str__(self):
        return '[%s] %s - %s > %s' % (self.data, self.aluno, self.anterior, self.situacao)

class TempoAluno(Log):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
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
def log_trans_aluno_financeira(sender, instance, **kwargs):
    anterior = Aluno.objects.get(pk=instance)
    print(anterior.nome)
    print('%s > %s' % (anterior.serie, instance.serie)) 