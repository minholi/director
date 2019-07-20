from django.contrib import admin
from .models import TipoAcao, Acao

@admin.register(TipoAcao)
class TipoAcaoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Acao)