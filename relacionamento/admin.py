from django.contrib import admin
from .models import Aluno, SitPresenca, SitNota, SitAtividade, SitFinanceira, SitMatricula, SitDocumentacao, SitAndamento, SitCadastral, Atendimento, Status
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import acoes.admin as aa
from suit import apps


class AlunoResource(resources.ModelResource):
    class Meta:
        model = Aluno


class AtendimentoInline(admin.StackedInline):
    model = Atendimento
    fields = ('obs', 'acao')
    extra = 1
    can_delete = False


@admin.register(Aluno)
class AlunoAdmin(ImportExportModelAdmin):
    list_display = ('ra', 'nome', 'curso', 'polo', 'presenca', 'nota', 'financeira', 'matricula', 'status')
    list_display_links = ('ra', 'nome')
    list_filter = ('curso', 'polo', 'curriculo', 'serie', 'presenca', 'nota', 'financeira', 'matricula', 'documentacao', 'andamento', 'cadastral', 'status')
    search_fields = ('ra', 'nome', 'cpf')
    resource_class = AlunoResource
    inlines = [AtendimentoInline,]
    """     
    readonly_fields = ('ra', 'nome', 'cpf', 'curso', 'curriculo', 'serie', 'polo')
    fieldsets = [
            (None, {
                'classes': ('suit-tab suit-tab-general',),
                'fields': [('nome', 'ra'), 'cpf', ('curso', 'curriculo', 'serie'), 'polo']
            }),
    ] 
    """

@admin.register(SitPresenca, SitNota, SitAtividade, SitFinanceira, SitMatricula, SitDocumentacao, SitAndamento, SitCadastral)
class SituacaoAdmin(aa.SituacaoAdmin):
    pass

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Status)