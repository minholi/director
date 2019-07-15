from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'

    menu = (
        ParentItem('Acadêmico', children=[
            ChildItem(model='academico.aluno'),
            ChildItem(model='relacionamento.atendimentoaluno'),
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
        ParentItem('Relacionamento', children=[
            ChildItem(model='relacionamento.acao'),
            ChildItem(model='relacionamento.tipoacao'),
        ], icon='fa fa-leaf'),
    )