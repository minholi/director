# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from academico.models import Aluno
from .models import TempoAluno

@shared_task
def aluno_temporal():
    alunos = Aluno.objects.all()

    for aluno in alunos:
        tempo = TempoAluno(
            aluno = aluno,
            presenca = aluno.presenca,
            nota = aluno.nota,
            financeira = aluno.financeira,
            matricula = aluno.matricula,
            documentacao = aluno.documentacao,
            andamento = aluno.andamento,
            cadastral = aluno.cadastral
        )
        tempo.save()