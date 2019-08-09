from django.shortcuts import render
from dal import autocomplete
from .models import Categoria

class CategoriaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Categoria.objects.none()

        qs = Categoria.objects.all()

        setor = self.forwarded.get('setor', None)

        if setor:
            qs = qs.filter(setor=setor)

        if self.q:
            qs = qs.filter(nome__istartswith=self.q)

        return qs