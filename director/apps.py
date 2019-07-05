from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'

    menu = (
        ParentItem('Acadêmico', children=[
            ChildItem(model='academico.aluno'),
        ], icon='fa fa-leaf'),
        ParentItem('Situações', children=[
            ChildItem(model='academico.presenca'),
            ChildItem(model='academico.nota'),
            ChildItem(model='academico.atividade'),
            ChildItem(model='academico.financeira'),
            ChildItem(model='academico.matricula'),
            ChildItem(model='academico.documentacao'),
            ChildItem(model='academico.cadastral'),
        ], icon='fa fa-leaf'),
    )