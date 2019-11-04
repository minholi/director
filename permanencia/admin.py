from django.contrib import admin
from .models import Aluno, SitPresenca, SitNota, SitAtividade, SitFinanceira, SitMatricula, SitDocumentacao, SitAndamento, SitCadastral, Atendimento, Status, Atividade, Disciplina, Cobranca
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import acoes.admin as aa
from suit import apps
from director.utils import ReadOnlyInline
from django.forms import ModelForm, Select
from suit.widgets import AutosizedTextarea


class AlunoResource(resources.ModelResource):
    class Meta:
        model = Aluno

class AtendimentoInlineForm(ModelForm):
    class Meta:
        widgets = {
            'obs': AutosizedTextarea(attrs={'rows': 2}),
            'acao': Select(attrs={'class': 'input-small'}),
        }

class AtendimentoInline(admin.StackedInline):
    model = Atendimento
    fields = ('obs', 'acao')
    extra = 1
    can_delete = False
    form = AtendimentoInlineForm

class AtividadeInline(ReadOnlyInline, admin.TabularInline):
    model = Atividade
    fields = ('ano', 'periodo', 'disciplina', 'data_entrega', 'nota', 'nota_max')
    suit_classes = 'suit-tab suit-tab-academico'

class DisciplinaInline(ReadOnlyInline, admin.TabularInline):
    model = Disciplina
    fields = ('disciplina', 'nome', 'ano', 'periodo', 'media', 'situacao')
    suit_classes = 'suit-tab suit-tab-academico'
    ordering = ('-ano', '-periodo')

class CobrancaInline(ReadOnlyInline, admin.TabularInline):
    model = Cobranca
    fields = ('cobranca', 'tipo', 'ano', 'mes', 'data_venc', 'data_pgto', 'val_pago', 'val_orig', 'val_final')
    suit_classes = 'suit-tab suit-tab-financeiro'
    ordering = ('-ano', '-mes')

class AlunoForm(ModelForm):
    class Meta:
        widgets = {
            'obs': AutosizedTextarea(attrs={'rows': 2}),
        }

@admin.register(Aluno)
class AlunoAdmin(ImportExportModelAdmin):
    list_display = ('ra', 'nome', 'curso', 'polo', 'presenca', 'nota', 'financeira', 'matricula', 'status')
    list_display_links = ('ra', 'nome')
    list_filter = ('curso', 'polo', 'curriculo', 'serie', 'presenca', 'nota', 'financeira', 'matricula', 'documentacao', 'andamento', 'cadastral', 'status')
    search_fields = ('ra', 'nome', 'cpf')
    resource_class = AlunoResource
    inlines = [AtividadeInline, DisciplinaInline, CobrancaInline, AtendimentoInline]
    form = AlunoForm

    fieldsets = (
        ('Ficha do aluno', {
            'classes': ('suit-tab suit-tab-ficha',),
            'fields': ('ra', 'nome', 'cpf', 'curso', 'curriculo', 'serie', 'polo', 'presenca', 'nota', 'financeira', 'matricula', 'documentacao', 'andamento', 'cadastral', 'obs', 'status')
        }),
    )

    suit_form_tabs = (
        ('ficha', 'Ficha'),
        ('academico', 'Acadêmico'),
        ('financeiro', 'Financeiro'),
    )

    class Media:
        css = {
            "all": ("//cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css",)
        }
        js = (
            '//cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js',
            '/static/js/alunoadmin.js',
        )

    # readonly_fields = ('ra', 'nome', 'cpf', 'curso', 'curriculo', 'serie', 'polo')
    # fieldsets = [
    #         (None, {
    #             'classes': ('suit-tab suit-tab-general',),
    #             'fields': [('nome', 'ra'), 'cpf', ('curso', 'curriculo', 'serie'), 'polo']
    #         }),
    # ] 


@admin.register(SitPresenca, SitNota, SitAtividade, SitFinanceira, SitMatricula, SitDocumentacao, SitAndamento, SitCadastral)
class SituacaoAdmin(aa.SituacaoAdmin):
    pass

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Status)
admin.site.register(Disciplina)
admin.site.register(Atividade)