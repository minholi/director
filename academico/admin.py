from django.contrib import admin
from academico.models import Aluno, Presenca, Nota, Atividade, Financeira, Matricula, Documentacao, Andamento, Cadastral
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class AlunoResource(resources.ModelResource):
    class Meta:
        model = Aluno

class AlunoAdmin(ImportExportModelAdmin):
    list_display = ('ra', 'nome', 'curso', 'polo', 'presenca', 'nota', 'financeira', 'matricula')
    list_display_links = ('ra', 'nome')
    list_filter = ('curso', 'polo', 'curriculo', 'serie', 'presenca', 'nota', 'financeira', 'matricula', 'documentacao', 'andamento', 'cadastral')
    search_fields = ('ra', 'nome', 'cpf')
    resource_class = AlunoResource

class SituacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'situacao', 'descricao')
    list_display_links = ('id', 'situacao')

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Presenca, SituacaoAdmin)
admin.site.register(Nota, SituacaoAdmin)
admin.site.register(Atividade, SituacaoAdmin)
admin.site.register(Financeira, SituacaoAdmin)
admin.site.register(Matricula, SituacaoAdmin)
admin.site.register(Documentacao, SituacaoAdmin)
admin.site.register(Andamento, SituacaoAdmin)
admin.site.register(Cadastral, SituacaoAdmin)