from django.urls import path
from .views import CategoriaAutocomplete
from .models import Chamado

urlpatterns = [
    path('chamado-categoria/', CategoriaAutocomplete.as_view(model=Chamado), name='chamado-categoria'),
]