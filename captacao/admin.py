from django.contrib import admin
from .models import Contato, Cadastral, Origem, Status, Atendimento, Conversao, AtendimentoAgendado
from django.db.models import OuterRef, Subquery

class AtendimentoInline(admin.StackedInline):
    model = Atendimento
    fields = ('obs', 'acao')
    extra = 1
    can_delete = False

class ConversaoInline(admin.TabularInline):
    model = Conversao
    fields = ('inscrito', 'acao', 'data')
    extra = 1

class AtendimentoAgendadoInline(admin.TabularInline):
    model = AtendimentoAgendado
    fields = ('data', 'acao', 'realizado', 'exito')
    extra = 1

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    inlines = [ConversaoInline, AtendimentoAgendadoInline, AtendimentoInline]
    list_display = ('nome', 'email', 'celular', 'status', 'nao_ligar', 'em_atendimento', 'prox_aa')

    def get_queryset(self, request):
        agendados = AtendimentoAgendado.objects.filter(
            contato=OuterRef('pk'), 
            realizado__isnull=True
        ).order_by('data')

        qs = super(ContatoAdmin, self).get_queryset(request)
        qs = qs.annotate(_prox_aa=Subquery(agendados.values('data')[:1]))
        return qs

    def save_formset(self, request, form, formset, change):
        """
        Salva o colaborador que realizou o cadastro do atendimento, conversão ou agendamento.
        """
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.colaborador = request.user
            instance.save()
        formset.save_m2m()

    def prox_aa(self, obj):
        return obj._prox_aa
    prox_aa.admin_order_field = 'prox_aa'
    prox_aa.short_description = 'próx. atend. agendado'

admin.site.register(Cadastral)
admin.site.register(Origem)
admin.site.register(Status)
admin.site.register(Atendimento)
admin.site.register(AtendimentoAgendado)
admin.site.register(Conversao)
