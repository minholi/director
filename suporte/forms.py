from django import forms
from suit.widgets import AutosizedTextarea
from estrutura.models import Setor
from .models import Chamado
from dal import autocomplete


class ChamadoForm(forms.ModelForm):

    class Meta:
        model = Chamado
        fields = ('__all__')
        widgets = {
            'categoria': autocomplete.ModelSelect2(url='chamado-categoria', forward=('setor',)),
            'informacoes': forms.Textarea(attrs={'class': 'summernote'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # desabilita campo se chamado não estiver editável
        if self.instance.status != 'rascunho':
            self.fields['informacoes'].widget.attrs['class'] = 'summernote-readonly'


class ComentarioInlineForm(forms.ModelForm):

    class Meta:
        widgets = {
            'mensagem': forms.Textarea(attrs={'class': 'summernote'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # desabilita campo de comentário já salvo
        if self.instance.id:
            self.fields['mensagem'].widget.attrs['class'] = 'summernote-readonly'