from django.contrib import admin
from .models import Inscrito, Cadastral, Atendimento, Status
import acoes.admin as aa

class AtendimentoInline(admin.StackedInline):
    model = Atendimento
    fields = ('obs', 'acao')
    extra = 1
    can_delete = False

@admin.register(Inscrito)
class InscritoAdmin(admin.ModelAdmin):
    inlines = [AtendimentoInline,]

@admin.register(Cadastral)
class SituacaoAdmin(aa.SituacaoAdmin):
    pass

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')

admin.site.register(Atendimento)
