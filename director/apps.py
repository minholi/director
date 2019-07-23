from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'

    menu = (
        ParentItem('Captação', children=[
            ChildItem(model='captacao.lead'),
            ChildItem(model='captacao.atendimento'),
            ChildItem(model='captacao.cadastral'),
            ChildItem(model='captacao.origem'),
            ChildItem(model='captacao.status'),
        ],),
        ParentItem('Ingresso', children=[
            ChildItem(model='ingresso.inscrito'),
            ChildItem(model='ingresso.atendimento'),
            ChildItem(model='ingresso.cadastral'),
        ],),
        ParentItem('Relacionamento', children=[
            ChildItem(model='relacionamento.aluno'),
            ChildItem(model='relacionamento.atendimento'),
        ],),
        ParentItem('Situações', children=[
            ChildItem(model='relacionamento.presenca'),
            ChildItem(model='relacionamento.nota'),
            ChildItem(model='relacionamento.atividade'),
            ChildItem(model='relacionamento.financeira'),
            ChildItem(model='relacionamento.matricula'),
            ChildItem(model='relacionamento.andamento'),
            ChildItem(model='relacionamento.documentacao'),
            ChildItem(model='relacionamento.cadastral'),
        ],),
        ParentItem('Ações', children=[
            ChildItem(model='acoes.acao'),
            ChildItem(model='acoes.tipoacao'),
        ],),
    )