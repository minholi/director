from django.contrib import admin
from .models import Chamado, Categoria
from django.forms import ModelForm
from .forms import ChamadoForm
from fsm_admin.mixins import FSMTransitionMixin

@admin.register(Chamado)
class ChamadoAdmin(FSMTransitionMixin, admin.ModelAdmin):
    form = ChamadoForm
    fsm_field = ['status',]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.solicitante = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Categoria)