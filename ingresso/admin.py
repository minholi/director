from django.contrib import admin
from .models import Inscrito, Cadastral, Atendimento

class AtendimentoInline(admin.StackedInline):
    model = Atendimento
    fields = ('obs', 'acao')
    extra = 1
    can_delete = False

@admin.register(Inscrito)
class InscritoAdmin(admin.ModelAdmin):
    inlines = [AtendimentoInline,]


admin.site.register(Atendimento)
admin.site.register(Cadastral)
