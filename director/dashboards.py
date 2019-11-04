from controlcenter import Dashboard, widgets
from permanencia.models import Aluno

class AlunoItemList(widgets.ItemList):
    model = Aluno
    list_display = ('ra', 'nome')

class MainDashboard(Dashboard):
    widgets = (
        AlunoItemList,
    )
    title = 'Visão Geral'