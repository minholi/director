from django.db import models
from estrutura.models import Setor, Usuario
from django_fsm import FSMField, transition
from django_currentuser.middleware import get_current_user

CHAMADO_CHOICES = (
    ('aberto', 'Aberto'),
    ('duplicado', 'Duplicado'),
    ('atendendo', 'Atendendo'),
    ('em_espera', 'Em espera'),
    ('fechado', 'Fechado'),
)

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, verbose_name='descrição')
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

class Chamado(models.Model):
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    assunto = models.CharField(max_length=255)
    informacoes = models.TextField(verbose_name='informações')
    solicitante = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    status = FSMField(default = 'aberto', choices = CHAMADO_CHOICES)

    def __str__(self):
        return self.assunto