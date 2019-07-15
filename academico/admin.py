from django.contrib import admin
from academico.models import Aluno, Presenca, Nota, Atividade, Financeira, Matricula, Documentacao, Andamento, Cadastral
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class AlunoResource(resources.ModelResource):
    class Meta:
        model = Aluno

@admin.register(Aluno)
class AlunoAdmin(ImportExportModelAdmin):
    list_display = ('ra', 'nome', 'curso', 'polo', 'presenca', 'nota', 'financeira', 'matricula')
    list_display_links = ('ra', 'nome')
    list_filter = ('curso', 'polo', 'curriculo', 'serie', 'presenca', 'nota', 'financeira', 'matricula', 'documentacao', 'andamento', 'cadastral')
    search_fields = ('ra', 'nome', 'cpf')
    resource_class = AlunoResource
    """     
    readonly_fields = ('ra', 'nome', 'cpf', 'curso', 'curriculo', 'serie', 'polo')
    fieldsets = [
            (None, {
                'classes': ('suit-tab suit-tab-general',),
                'fields': [('nome', 'ra'), 'cpf', ('curso', 'curriculo', 'serie'), 'polo']
            }),
    ] 
    """

@admin.register(Presenca, Nota, Atividade, Financeira, Matricula, Documentacao, Andamento, Cadastral)
class SituacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'situacao', 'descricao')
    list_display_links = ('id', 'situacao')
