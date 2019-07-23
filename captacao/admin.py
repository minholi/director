from django.contrib import admin
from .models import Lead, Cadastral, Origem, Status, Atendimento, Conversao

class AtendimentoInline(admin.StackedInline):
    model = Atendimento
    fields = ('obs', 'acao')
    extra = 1
    can_delete = False

class ConversaoInline(admin.TabularInline):
    model = Conversao
    extra = 1

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    inlines = [ConversaoInline, AtendimentoInline]

admin.site.register(Cadastral)
admin.site.register(Origem)
admin.site.register(Status)
admin.site.register(Atendimento)
admin.site.register(Conversao)
