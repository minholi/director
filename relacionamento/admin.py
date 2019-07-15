from django.contrib import admin
from .models import AtendimentoAluno, TipoAcao, Acao

admin.site.register(AtendimentoAluno)
admin.site.register(TipoAcao)
admin.site.register(Acao)