from django.contrib import admin
from django.db.models import Q
from .models import Chamado, Categoria, Anexo, Comentario
from .forms import ChamadoForm, ComentarioInlineForm
from fsm_admin.mixins import FSMTransitionMixin


class ComentarioInline(admin.StackedInline):
    model = Comentario
    suit_classes = 'suit-tab suit-tab-comentarios'
    fields = ['mensagem',]
    extra = 1
    form = ComentarioInlineForm

    def has_delete_permission(self, request, obj=None):
        if obj and obj.status != 'rascunho':
                return False
        return super(ComentarioInline, self).has_delete_permission(request, obj)

    def has_add_permission(self, request, obj=None):
        if obj and obj.status == 'fechado':
                return False
        return super(ComentarioInline, self).has_delete_permission(request, obj)

class AnexoInline(admin.TabularInline):
    model = Anexo
    suit_classes = 'suit-tab suit-tab-anexos'
    readonly_fields = ['usuario',]
    extra = 1

    def has_delete_permission(self, request, obj=None):
        if obj and obj.status != 'rascunho':
                return False
        return super(AnexoInline, self).has_delete_permission(request, obj)

    def has_add_permission(self, request, obj=None):
        if obj and obj.status == 'fechado':
                return False
        return super(AnexoInline, self).has_delete_permission(request, obj)

@admin.register(Chamado)
class ChamadoAdmin(FSMTransitionMixin, admin.ModelAdmin):
    list_display = ('assunto', 'setor', 'categoria', 'solicitante', 'responsavel', 'data_abertura', 'data_atendimento', 'data_fechamento', 'status')
    form = ChamadoForm
    inlines = [AnexoInline, ComentarioInline]
    fsm_field = ['status',]
    autocomplete_fields = ('relacionado',)
    search_fields = ('assunto', 'relacionado')
    list_filter = ('setor', 'categoria', 'solicitante', 'status')
    readonly_fields = ['solicitante', 'responsavel', 'data_abertura', 'data_atendimento', 'data_fechamento', 'status']

    suit_form_tabs = (
        ('detalhes', 'Detalhes'),
        ('anexos', 'Anexos'),
        ('comentarios', 'Comentários')
    )

    fieldsets = (
        ('Detalhes do chamado', {
            'classes': ('suit-tab suit-tab-detalhes',),
            'fields': ('assunto', 'setor', 'categoria', 'informacoes', 'relacionado', 'solicitante', 'responsavel', 'data_abertura', 'data_atendimento', 'data_fechamento', 'status')
        }),
    )

    def get_queryset(self, request):
        qs = super(ChamadoAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(Q(solicitante__setor=request.user.setor) | Q(setor=request.user.setor))

        return qs

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = self.readonly_fields
        if obj and obj.status != 'rascunho':
            readonly_fields = readonly_fields + ['setor', 'categoria', 'assunto', 'relacionado']

        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        if obj and obj.status != 'rascunho':
                return False
        return super(ChamadoAdmin, self).has_delete_permission(request, obj)

    def get_inline_formsets(self, request, formsets, inline_instances, obj=None):
        inline_admin_formsets = []
        for inline, formset in zip(inline_instances, formsets):
            fieldsets = list(inline.get_fieldsets(request, obj))
            readonly = list(inline.get_readonly_fields(request, obj))
            prepopulated = dict(inline.get_prepopulated_fields(request, obj))
            inline_admin_formset = admin.helpers.InlineAdminFormSet(
                inline, formset, fieldsets, prepopulated, readonly,
                model_admin=self,
            )

            if obj:
                if isinstance(inline, AnexoInline):
                    for form in inline_admin_formset.forms:
                        if form.instance.usuario_id not in (request.user.id, None) or obj.status == 'fechado':
                            form.fields['descricao'].widget.attrs['readonly'] = True
                            form.fields['arquivo'].widget.attrs['readonly'] = True

                if isinstance(inline, ComentarioInline):
                    for form in inline_admin_formset.forms:
                        if form.instance.usuario_id not in (request.user.id, None) or obj.status == 'fechado':
                            form.fields['mensagem'].widget.attrs['readonly'] = True

            inline_admin_formsets.append(inline_admin_formset)
        return inline_admin_formsets

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            if isinstance(instance, (Anexo, Comentario)):
                instance.usuario = request.user

            instance.save()
        formset.save_m2m()
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.solicitante = request.user

        super().save_model(request, obj, form, change)

admin.site.register(Categoria)