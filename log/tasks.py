# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from relacionamento.models import Aluno
from .models import TempoAluno
from django.utils import timezone
from django.db import transaction

@shared_task
@transaction.atomic
def aluno_temporal():
    ontem = timezone.now() - timezone.timedelta(days=1)
    alunos = Aluno.objects.all()

    for aluno in alunos:
        TempoAluno.objects.update_or_create(
            aluno = aluno,
            data = ontem.date(),
            hora = '23:59:59',
            defaults = {
                'presenca': aluno.presenca,
                'nota': aluno.nota,
                'financeira': aluno.financeira,
                'matricula': aluno.matricula,
                'documentacao': aluno.documentacao,
                'andamento': aluno.andamento,
                'cadastral': aluno.cadastral,
            }
        )

    return '%s aluno(s)' % alunos.count()