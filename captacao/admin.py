from django.contrib import admin
from .models import Contato, Cadastral, Origem, Status, Atendimento, Conversao, AtendimentoAgendado

class AtendimentoInline(admin.StackedInline):
    model = Atendimento
    fields = ('obs', 'acao')
    extra = 1
    can_delete = False

class ConversaoInline(admin.TabularInline):
    model = Conversao
    extra = 1

class AtendimentoAgendadoInline(admin.TabularInline):
    model = AtendimentoAgendado
    fields = ('data', 'acao', 'realizado', 'exito')
    extra = 1

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    inlines = [ConversaoInline, AtendimentoAgendadoInline, AtendimentoInline]
    list_display = ('nome', 'email', 'celular', 'status', 'nao_ligar', 'em_atendimento', 'proximo_atendimento_agendado')

admin.site.register(Cadastral)
admin.site.register(Origem)
admin.site.register(Status)
admin.site.register(Atendimento)
admin.site.register(AtendimentoAgendado)
admin.site.register(Conversao)
