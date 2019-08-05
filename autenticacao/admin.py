from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Setor, Unidade

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    local_fieldsets = (
        (('Informações extras'), {'fields': ('setor', 'unidade')}),
    )
    fieldsets = UserAdmin.fieldsets + local_fieldsets

admin.site.register(Setor)
admin.site.register(Unidade)