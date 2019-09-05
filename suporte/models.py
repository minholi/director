from django.db import models
from estrutura.models import Setor, Usuario
from django_fsm import FSMField, transition
from django_currentuser.middleware import get_current_user # TODO: validar usuario para não atender a si proprio
from django_fsm_log.decorators import fsm_log_by, fsm_log_description
from django.utils import timezone

CHAMADO_CHOICES = (
    ('rascunho', 'Rascunho'),
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
    relacionado = models.ForeignKey("self", null=True, blank=True, on_delete=models.PROTECT, help_text='Informe o chamado caso exista relação com outro já informado ou se trate de um chamado duplicado')
    solicitante = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='solicitantes')
    responsavel = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.PROTECT, related_name='responsaveis', verbose_name=u'responsável')
    data_abertura = models.DateTimeField(verbose_name=u'Data de abertura', null=True, blank=True)
    data_atendimento = models.DateTimeField(null=True, blank=True, verbose_name=u'Data de atendimento')
    data_fechamento = models.DateTimeField(null=True, blank=True, verbose_name=u'Data de fechamento')
    status = FSMField(default = 'rascunho', choices = CHAMADO_CHOICES)

    def __str__(self):
        return self.assunto

    class Meta:
        permissions = (
            ("can_atender", "Pode atender chamados"),
        )

    @fsm_log_by
    @fsm_log_description
    @transition(field=status, source='rascunho', target='aberto', custom={'button_name':'Abrir chamado'})
    def abrir(self, description=None, by=None):
        description = 'Aberto por %s' % by
        self.solicitante = by
        self.data_abertura = timezone.now()

    @fsm_log_by
    @fsm_log_description
    @transition(field=status, source='aberto', target='rascunho', custom={'button_name':'Alterar chamado'})
    def editar(self, description=None, by=None):
        description = 'Alterado por %s' % by
        self.solicitante = by
        self.data_abertura = None

    @fsm_log_by
    @fsm_log_description
    @transition(field=status, source='aberto', target='atendendo', permission='suporte.can_atender', custom={'button_name':'Atender chamado'})
    def atender(self, description=None, by=None):
        description = 'Atendido por %s' % by
        self.responsavel = by
        self.data_atendimento = timezone.now()

    @fsm_log_by
    @fsm_log_description
    @transition(field=status, source=['aberto', 'atendendo', 'em_espera'], target='duplicado', custom={'button_name':'Marcar como duplicado'}) # TODO: Tratar permissão para marcar como duplicado
    def marcar_duplicado(self, description=None, by=None):
        description = 'Marcado como duplicado por %s' % by
        self.responsavel = by

    @fsm_log_by
    @fsm_log_description
    @transition(field=status, source=['aberto', 'atendendo'], target='em_espera', custom={'button_name':'Colocar em espera'}) # TODO: Tratar permissão para colocar em espera
    def colocar_em_espera(self, description=None, by=None):
        description = 'Colocado em espera por %s' % by
        self.responsavel = by

    @fsm_log_by
    @fsm_log_description
    @transition(field=status, source=['atendendo', 'em_espera', 'duplicado', 'fechado'], target='aberto', custom={'button_name':'Reabrir chamado'}) # TODO: Tratar permissão para reabrir
    def reabrir(self, description=None, by=None):
        description = 'Reaberto por %s' % by
        self.responsavel = by
        self.data_atendimento = None

    @fsm_log_by
    @fsm_log_description
    @transition(field=status, source='aberto', target='fechado', custom={'button_name':'Fechar chamado'}) # TODO: Tratar permissão para fechar
    def fechar(self, description=None, by=None):
        description = 'Fechado por %s' % by
        self.responsavel = by
        self.data_fechamento = timezone.now()


class Anexo(models.Model):
    descricao = models.CharField(max_length=255, verbose_name='Descrição')
    arquivo = models.FileField(upload_to='suporte')
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    chamado = models.ForeignKey(Chamado, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao

class Comentario(models.Model):
    comentario = models.TextField(verbose_name=u'Comentário')
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    chamado = models.ForeignKey(Chamado, on_delete=models.PROTECT)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'comentário'

    def __str__(self):
        return u'%s em %s' % (self.usuario, self.data)