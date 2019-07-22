from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'

    menu = (
        ParentItem('Captação', children=[
            ChildItem(model='captacao.lead'),
            ChildItem(model='captacao.cadastral'),
        ], icon='fa fa-leaf'),
        ParentItem('Ingresso', children=[
            ChildItem(model='ingresso.candidato'),
            ChildItem(model='ingresso.cadastral'),
        ], icon='fa fa-leaf'),
        ParentItem('Relacionamento', children=[
            ChildItem(model='relacionamento.aluno'),
            ChildItem(model='relacionamento.atendimento'),
        ], icon='fa fa-leaf'),
        ParentItem('Situações', children=[
            ChildItem(model='relacionamento.presenca'),
            ChildItem(model='relacionamento.nota'),
            ChildItem(model='relacionamento.atividade'),
            ChildItem(model='relacionamento.financeira'),
            ChildItem(model='relacionamento.matricula'),
            ChildItem(model='relacionamento.documentacao'),
            ChildItem(model='relacionamento.cadastral'),
        ], icon='fa fa-leaf'),
        ParentItem('Ações', children=[
            ChildItem(model='acoes.acao'),
            ChildItem(model='acoes.tipoacao'),
        ], icon='fa fa-leaf'),
    )