from django.contrib import admin
from base.models import Pessoa
from django.forms import ModelForm
from localflavor.br.forms import BRCPFField

class PessoaForm(ModelForm):
    cpf = BRCPFField()

    class Meta:
        model = Pessoa
        fields = ['nome', 'cpf']


class PessoaAdmin(admin.ModelAdmin):
    form = PessoaForm

admin.site.register(Pessoa, PessoaAdmin)
