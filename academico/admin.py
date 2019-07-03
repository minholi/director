from django.contrib import admin
from academico.models import Aluno, Presenca, Desempenho, Financeiro, Matricula, Documentacao, Andamento, Situacao
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class AlunoResource(resources.ModelResource):
    class Meta:
        model = Aluno

class AlunoAdmin(ImportExportModelAdmin):
    list_display = ('ra', 'nome', 'curso', 'polo', 'presenca', 'desempenho', 'financeiro', 'matricula')
    list_display_links = ('ra', 'nome')
    list_filter = ('curso', 'polo', 'curriculo', 'serie', 'presenca', 'desempenho', 'financeiro', 'matricula', 'documentacao', 'andamento', 'situacao')
    search_fields = ('ra', 'nome', 'cpf')
    resource_class = AlunoResource

class PresencaAdmin(admin.ModelAdmin):
    list_display = ('id', 'situacao', 'descricao')
    list_display_links = ('id', 'situacao')

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Presenca, PresencaAdmin)
admin.site.register(Desempenho)
admin.site.register(Financeiro)
admin.site.register(Matricula)
admin.site.register(Documentacao)
admin.site.register(Andamento)
admin.site.register(Situacao)