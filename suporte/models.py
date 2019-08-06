from django.db import models
from estrutura.models import Setor, Usuario
from django_fsm import FSMField, transition
from django_currentuser.middleware import get_current_user

CHAMADO_CHOICES = (
    ('aberto', 'Aberto'),
    ('atendendo', 'Atendendo'),
    ('em_espera', 'Em espera'),
    ('fechado', 'Fechado'),
)

class Chamado(models.Model):
    assunto = models.CharField(max_length=100)
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)
    status = FSMField(default = 'aberto', choices = CHAMADO_CHOICES)
