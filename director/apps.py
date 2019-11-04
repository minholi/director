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
        ParentItem('Permanência', children=[
            ChildItem(model='permanencia.aluno'),
            ChildItem(model='permanencia.atendimento'),
        ],),
        ParentItem('Situações', children=[
            ChildItem(model='permanencia.sitpresenca'),
            ChildItem(model='permanencia.sitnota'),
            ChildItem(model='permanencia.sitatividade'),
            ChildItem(model='permanencia.sitfinanceira'),
            ChildItem(model='permanencia.sitmatricula'),
            ChildItem(model='permanencia.sitandamento'),
            ChildItem(model='permanencia.sitdocumentacao'),
            ChildItem(model='permanencia.sitcadastral'),
            ChildItem(model='permanencia.status'),
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