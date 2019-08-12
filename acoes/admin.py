from django.contrib import admin
from .models import TipoAcao, Acao

@admin.register(TipoAcao)
class TipoAcaoAdmin(admin.ModelAdmin):
    pass

class SituacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'situacao', 'descricao', 'conversivel', 'conversao')
    list_display_links = ('id', 'situacao')

admin.site.register(Acao)