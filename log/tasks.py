# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from captacao.models import Contato
from ingresso.models import Inscrito
from permanencia.models import Aluno
from .models import TempoContato, TempoInscrito, TempoAluno
from django.utils import timezone
from django.db import transaction

@shared_task
@transaction.atomic
def contato_temporal():
    ontem = timezone.now() - timezone.timedelta(days=1)
    contatos = Contato.objects.all()

    for contato in contatos:
        TempoContato.objects.update_or_create(
            contato = contato,
            data = ontem.date(),
            hora = '23:59:59',
            defaults = {
                'cadastral': contato.cadastral,
            }
        )

    return '%s contato(s)' % contatos.count()

@shared_task
@transaction.atomic
def inscrito_temporal():
    ontem = timezone.now() - timezone.timedelta(days=1)
    inscritos = Inscrito.objects.all()

    for inscrito in inscritos:
        TempoInscrito.objects.update_or_create(
            inscrito = inscrito,
            data = ontem.date(),
            hora = '23:59:59',
            defaults = {
                'cadastral': inscrito.cadastral,
            }
        )

    return '%s inscrito(s)' % inscritos.count()

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