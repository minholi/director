from django.contrib import admin
from .models import Aluno, SitPresenca, SitNota, SitAtividade, SitFinanceira, SitMatricula, SitDocumentacao, SitAndamento, SitCadastral, Atendimento, Status, Atividade, Disciplina
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import acoes.admin as aa
from suit import apps
from director.utils import ReadOnlyInline


class AlunoResource(resources.ModelResource):
    class Meta:
        model = Aluno


class AtendimentoInline(admin.StackedInline):
    model = Atendimento
    fields = ('obs', 'acao')
    extra = 1
    can_delete = False

class AtividadeInline(ReadOnlyInline, admin.TabularInline):
    model = Atividade
    fields = ('ano', 'periodo', 'disciplina', 'data_entrega', 'nota', 'nota_max')
    suit_classes = 'suit-tab suit-tab-academico'

class DisciplinaInline(ReadOnlyInline, admin.TabularInline):
    model = Disciplina
    fields = ('disciplina', 'nome', 'ano', 'periodo', 'media', 'situacao')
    suit_classes = 'suit-tab suit-tab-academico'
    ordering = ('-ano', '-periodo')

@admin.register(Aluno)
class AlunoAdmin(ImportExportModelAdmin):
    list_display = ('ra', 'nome', 'curso', 'polo', 'presenca', 'nota', 'financeira', 'matricula', 'status')
    list_display_links = ('ra', 'nome')
    list_filter = ('curso', 'polo', 'curriculo', 'serie', 'presenca', 'nota', 'financeira', 'matricula', 'documentacao', 'andamento', 'cadastral', 'status')
    search_fields = ('ra', 'nome', 'cpf')
    resource_class = AlunoResource
    inlines = [AtividadeInline, DisciplinaInline, AtendimentoInline]

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


    # readonly_fields = ('ra', 'nome', 'cpf', 'curso', 'curriculo', 'serie', 'polo')
    # fieldsets = [
    #         (None, {
    #             'classes': ('suit-tab suit-tab-general',),
    #             'fields': [('nome', 'ra'), 'cpf', ('curso', 'curriculo', 'serie'), 'polo']
    #         }),
    # ] 


    class Media:
        css = {
            "all": ("//cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css",)
        }
        js = (
            '//cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js',
            '/static/js/scripts.js',
        )




@admin.register(SitPresenca, SitNota, SitAtividade, SitFinanceira, SitMatricula, SitDocumentacao, SitAndamento, SitCadastral)
class SituacaoAdmin(aa.SituacaoAdmin):
    pass

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Status)
admin.site.register(Disciplina)