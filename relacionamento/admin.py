from django.contrib import admin
from .models import Aluno, Presenca, Nota, Atividade, Financeira, Matricula, Documentacao, Andamento, Cadastral, Atendimento
from import_export import resources
from import_export.admin import ImportExportModelAdmin
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
    list_display = ('ra', 'nome', 'curso', 'polo', 'presenca', 'nota', 'financeira', 'matricula')
    list_display_links = ('ra', 'nome')
    list_filter = ('curso', 'polo', 'curriculo', 'serie', 'presenca', 'nota', 'financeira', 'matricula', 'documentacao', 'andamento', 'cadastral')
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

@admin.register(Presenca, Nota, Atividade, Financeira, Matricula, Documentacao, Andamento, Cadastral)
class SituacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'situacao', 'descricao')
    list_display_links = ('id', 'situacao')

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    pass
