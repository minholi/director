from selectable.base import ModelLookup
from selectable.registry import registry
from selectable.decorators import login_required
from .models import Categoria

@login_required
class CategoriaLookup(ModelLookup):
    model = Categoria
    search_fields = ('nome__icontains',)
    
    def get_query(self, request, term):
        results = super(CategoriaLookup, self).get_query(request, term)
        setor = request.GET.get('setor', '')
        if setor:
            results = results.filter(setor=setor)
        return results
    
    def get_item_label(self, item):
        return "%s, %s" % (item.nome, item.setor)

registry.register(CategoriaLookup)
