from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'

    menu = (
        ParentItem('Captação', children=[
            ChildItem(model='captacao.contato'),
            ChildItem(model='captacao.atendimento'),
            ChildItem('Atend. Agendados', model='captacao.atendimentoagendado'),
            ChildItem(model='captacao.conversao'),
            ChildItem(model='captacao.sitcadastral'),
            ChildItem(model='captacao.origem'),
            ChildItem(model='captacao.status'),
        ],),
        ParentItem('Ingresso', children=[
            ChildItem(model='ingresso.inscrito'),
            ChildItem(model='ingresso.atendimento'),
            ChildItem(model='ingresso.sitcadastral'),
            ChildItem(model='ingresso.status'),
        ],),
        ParentItem('Relacionamento', children=[
            ChildItem(model='relacionamento.aluno'),
            ChildItem(model='relacionamento.atendimento'),
        ],),
        ParentItem('Situações', children=[
            ChildItem(model='relacionamento.sitpresenca'),
            ChildItem(model='relacionamento.sitnota'),
            ChildItem(model='relacionamento.sitatividade'),
            ChildItem(model='relacionamento.sitfinanceira'),
            ChildItem(model='relacionamento.sitmatricula'),
            ChildItem(model='relacionamento.sitandamento'),
            ChildItem(model='relacionamento.sitdocumentacao'),
            ChildItem(model='relacionamento.sitcadastral'),
            ChildItem(model='relacionamento.status'),
        ],),
        ParentItem('Ações', children=[
            ChildItem(model='acoes.acao'),
            ChildItem(model='acoes.tipoacao'),
        ],),
        ParentItem('Suporte', children=[
            ChildItem(model='suporte.chamado'),
            ChildItem(model='suporte.categoria'),
        ],),
    )