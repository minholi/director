from django import forms
from estrutura.models import Setor
from .models import Chamado
from dal import autocomplete


class ChamadoForm(forms.ModelForm):

    class Meta:
        model = Chamado
        fields = ('__all__')
        widgets = {
            'categoria': autocomplete.ModelSelect2(url='chamado-categoria', forward=('setor',))
        }