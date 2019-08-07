from django import forms
from estrutura.models import Setor
from selectable.forms import AutoCompleteSelectField, AutoComboboxSelectWidget
from .lookups import CategoriaLookup


class ChamadoForm(forms.ModelForm):
    categoria = AutoCompleteSelectField(
        lookup_class=CategoriaLookup,
        label='Categoria',
        widget=AutoComboboxSelectWidget
    )
    class Meta:
        js = ('js/scripts.js',)