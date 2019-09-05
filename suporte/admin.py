from django.contrib import admin
from .models import Chamado, Categoria, Anexo
from django.forms import ModelForm
from .forms import ChamadoForm
from fsm_admin.mixins import FSMTransitionMixin

class AnexoInline(admin.TabularInline):
    model = Anexo
    suit_classes = 'suit-tab suit-tab-anexos'
    readonly_fields = ['usuario',]
    extra = 1

@admin.register(Chamado)
class ChamadoAdmin(FSMTransitionMixin, admin.ModelAdmin):
    list_display = ('assunto', 'setor', 'categoria', 'solicitante', 'responsavel', 'data_abertura', 'data_atendimento', 'data_fechamento', 'status')
    form = ChamadoForm
    inlines = [AnexoInline,]
    fsm_field = ['status',]
    autocomplete_fields = ('relacionado',)
    search_fields = ('assunto', 'relacionado')
    list_filter = ('setor', 'categoria', 'solicitante', 'status')
    readonly_fields = ['solicitante', 'responsavel', 'data_abertura', 'data_atendimento', 'data_fechamento', 'status']

    suit_form_tabs = (
        ('detalhes', 'Detalhes'),
        ('anexos', 'Anexos')
    )

    fieldsets = (
        ('Detalhes do chamado', {
            'classes': ('suit-tab suit-tab-detalhes',),
            'fields': ('assunto', 'setor', 'categoria', 'informacoes', 'relacionado', 'solicitante', 'responsavel', 'data_abertura', 'data_atendimento', 'data_fechamento', 'status')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = self.readonly_fields
        if not obj.status == 'rascunho':
            readonly_fields = readonly_fields + ['setor', 'categoria', 'assunto', 'informacoes', 'relacionado']

        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        try:
            if obj.status != 'rascunho':
                return False
            return super(ChamadoAdmin, self).has_delete_permission(request, obj)
        except AttributeError:
            pass

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            if isinstance(instance, Anexo):
                instance.usuario = request.user

            instance.save()
        formset.save_m2m()
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.solicitante = request.user

        super().save_model(request, obj, form, change)

admin.site.register(Categoria)