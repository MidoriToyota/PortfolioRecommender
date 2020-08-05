## Pacotes #########################################################################################################################################
import base64
import io
import os
import urllib3
from urllib.parse import quote
import pandas as pd
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_html_components as html
from funcoes_auxiliares import *
import plotly.io as pio
import plotly.offline as pyo
import plotly.graph_objs as go
from collections import Counter

## Carregar dados  ################################################################################################################################

# Dataset utilizado apenas para gerar gráficos
df_market = pd.read_csv('data/df_market.csv', index_col='id')


# Dataset utilizado para criar o modelo
# dividido em 3 pois o github não aceita arquivos maiores que 100 MB.
df1_preprocessed = pd.read_csv('data/df1_preprocessed.csv', index_col='id')
df2_preprocessed = pd.read_csv('data/df2_preprocessed.csv', index_col='id')
df3_preprocessed = pd.read_csv('data/df3_preprocessed.csv', index_col='id')
df4_preprocessed = pd.read_csv('data/df4_preprocessed.csv', index_col='id')
df5_preprocessed = pd.read_csv('data/df5_preprocessed.csv', index_col='id')
df6_preprocessed = pd.read_csv('data/df6_preprocessed.csv', index_col='id')
df7_preprocessed = pd.read_csv('data/df7_preprocessed.csv', index_col='id')
df8_preprocessed = pd.read_csv('data/df8_preprocessed.csv', index_col='id')
df9_preprocessed = pd.read_csv('data/df9_preprocessed.csv', index_col='id')
df10_preprocessed = pd.read_csv('data/df10_preprocessed.csv', index_col='id')

frames = [df1_preprocessed, df2_preprocessed, df3_preprocessed, df4_preprocessed, df5_preprocessed, df6_preprocessed, df7_preprocessed, df8_preprocessed, df9_preprocessed, df10_preprocessed]
df_preprocessed = pd.concat(frames)

## Configurações iniciais  ##########################################################################################################################

'''Funções para criar o esqueleto do app (cabeçalho e corpo vazio) '''
pio.templates.default = "plotly_dark"

try:
    from layout_helper import run_standalone_app
except ModuleNotFoundError:
    from .layout_helper import run_standalone_app

def header_colors():
    return {'bg_color': '#262B3D', 'font_color': '#FFF', 'light_logo': True}

## Gráficos iniciais  ##########################################################################################################################

data_inicial = [go.Indicator(
    number={'font':{'color':'#1F2132'}},
    mode = "number",
    value = 0,
    title = "")]

layout_inicial = go.Layout(paper_bgcolor='#1F2132', plot_bgcolor='#1F2132')

fig_inicial = go.Figure(data=data_inicial, layout=layout_inicial)

## Layout do site ##################################################################################################################################

def layout():
    return html.Div(id='circos-body', className='app-body', children=[
        html.Div(id='circos-control-tabs', className='control-tabs', children=[
            dcc.Tabs(id='circos-tabs', value='what-is', children=[

## Sobre o app e Sobre a autora ----------------------------------------------------------------------------------------------------------------------

                dcc.Tab(
                    label='Sobre',
                    value='what-is',
                    children=html.Div(className='control-tab', children=[
                        html.H4(className='what-is', children="Sobre o App"),

                        html.P('''O Portfolio Recommender é uma aplicação web que fornece um
                               serviço automatizado de recomendação de leads para um usuário
                               dado sua atual lista de clientes (Portfólio).'''),
                        html.P('''Ele foi criado para solucionar o problema de empresas
                                que gostariam de saber quem são as demais empresas em um
                                determinado mercado (população) que tem maior probabilidade
                                de se tornarem seus próximos clientes. Ou seja, quem são os
                                leads mais aderentes dadas as características dos clientes
                                presentes no portfólio do usuário.'''),
                        html.P('''Além de retornar uma lista de empresas recomendadas,
                                o Portfolio Recommender também fornece a visualização completa
                                das principais características das empresas do portfolio.'''),

                        html.P('''Notebooks relacionados:'''),
                        html.Div([html.A('Análise exploratória e tratamento', href='https://midoritoyota.netlify.app/')]),
                        html.Div([html.A('Pre processamento', href='https://midoritoyota.netlify.app/')]),
                        html.Div([html.A('Criação do modelo', href='https://midoritoyota.netlify.app/')]),
                        html.Div([html.A('Visualização dos resultados 1', href='https://midoritoyota.netlify.app/')]),
                        html.Div([html.A('Visualização dos restultados 2', href='https://midoritoyota.netlify.app/')], style={'margin-bottom': '40px'}),

                        html.H4(className='what-is', children="Sobre a Autora"),

                        html.P('''Oi, meu nome é Midori! Atualmente estou em processo de
                                transição de carreira da Engenharia Civil para Ciência
                                de Dados e, por esse motivo, realizo diversos projetos para
                                botar em prática o que venho aprendendo sobre essa nova área.
                                Desenvolvi o Portfolio Recommender como solução de um
                                problema proposto no projeto final do Aceleradev de
                                Data Science. Se quiser saber mais sobre o projeto, você
                                pode ver o código fonte acessando o meu portfolio no link
                                abaixo. Também, estou aberta a novas oportunidades, então,
                                se deseja me conhecer melhor me adicione no linkedin e
                                vamos bater um papo! '''),

                        html.Div([
                            'Portfolio: ',
                            html.A('midoritoyota.netlify.app', href='https://midoritoyota.netlify.app/')
                        ]),

                        html.Div([
                            'Linkedin: ',
                            html.A('www.linkedin.com/in/midoritoyota', href='https://www.linkedin.com/in/midoritoyota')
                        ]),
                        html.Br()
                    ])
                ),

## Dados - Updolad e Download ----------------------------------------------------------------------------------------------------------------------

                dcc.Tab(
                    label='Dados',
                    value='data',
                    children=html.Div(className='control-tab', children=[
                        html.Div(className='app-controls-block', children=[
                            html.Div(className='app-controls-name', children='Upload')
                        ]),
                        html.A(
                            html.Button(
                                id='circos-download-button',
                                className='control-download',
                                children="Download dos dados de Exemplo"
                            ),
                            href="https://drive.google.com/drive/folders/1_2iEzn03ID3XGTsQmSvOBnl32fg02efj?usp=sharing",
                        ),

                        html.Div(id='circos-uploaded-data', children=[
                            dcc.Upload(
                                id="upload-data",
                                className='control-upload',
                                children=html.Div(
                                    ['''Escolha ou solte o arquivo .CSV aqui!''']
                                ), multiple=True),
                        ]),
                        dcc.Loading(id='carregamento-sucesso', style={'margin-top': '140px'}),
                    ])
                ),

## Visualização dos resultados ----------------------------------------------------------------------------------------------------------------------

                dcc.Tab(
                    label='Análise',
                    value='graph',
                    children=html.Div(className='control-tab', children=[
                        html.Div(className='app-controls-block', children=[
                            html.Div(className='app-controls-name',  children='Variáveis Categóricas'),
                            html.Div(className='espacamento'),
                            dcc.RadioItems(id='selecao-dataset',
                                            options=[
                                                {'label': 'Portfólio', 'value': 'portfolio'},
                                                {'label':'Recomendacões', 'value': 'recomendacoes'},
                                            ], value='portfolio', labelStyle={'display': 'inline-block', 'margin':'0px 10px 0px 10px'}),
                            html.Div(className='espacamento'),
                            dcc.Dropdown(id='analise-categorica',
                                            options=[
                                                {'label': 'Natureza jurídica', 'value': 'de_natureza_juridica'},
                                                {'label': 'Ramo de atividade', 'value': 'de_ramo'},
                                                {'label': 'Saúde tributária', 'value': 'de_saude_tributaria'},
                                                {'label': 'Nível de atividade', 'value': 'de_nivel_atividade'}
                                            ], value='de_natureza_juridica'),
                            html.Hr(),
                            html.Div(className='app-controls-name',  children='Variáveis Contínuas'),
                            html.Div(className='espacamento'),
                            dcc.RadioItems(id='selecao-escala',
                                            options=[
                                                {'label': 'Linear', 'value': '-'},
                                                {'label': 'Logaritimica', 'value': 'log'},
                                            ], value='-', labelStyle={'display': 'inline-block', 'margin':'0px 10px 0px 10px'}),
                            html.Div(className='espacamento'),
                            dcc.Dropdown(id='analise-continua',
                                            options=[
                                                {'label': 'Idade da empresa (anos)', 'value': 'idade_empresa_anos'},
                                                {'label': 'Faturamento estimado (R$)', 'value': 'vl_faturamento_estimado_aux'},
                                                {'label': 'Quantidade de filiais (un)', 'value': 'qt_filiais'}
                                            ], value='idade_empresa_anos'),
                        ]),
                    ]),
                ),

## Overview ----------------------------------------------------------------------------------------------------------------------

            ])
        ]),

        html.Div(id='espaco-graficos',
        children=[html.Div(id='pano1', children= dcc.Graph(id='grafico1', figure=fig_inicial)),
                html.Div(id='pano2', children= dcc.Graph(id='grafico2', figure=fig_inicial)),
                html.Div(id='pano3', children= dcc.Graph(id='grafico3', figure=fig_inicial))
    ])
])

## Callbacks #########################################################################################################################################

def callbacks(_app):

    ## Ler arquivo e gerar lista ----------------------------------------------------------------------------------------------------------------------

    @_app.callback(Output("carregamento-sucesso", 'children'),
                  [Input('upload-data', 'contents')],
                  [State('upload-data', 'filename')])
    def update_output(list_of_contents, list_of_names):
        if list_of_contents is None:
            return ""
        else:
            # Criar variáveis globais
            global df_ptf
            global df_sim
            global df_treino


            # Ler arquivo inserido pelo usuário
            df_ptf = [parse_contents(c, n) for c, n in zip(list_of_contents, list_of_names)]
            df_ptf = df_ptf[0]
            df_treino, df_sim, lista_ids  = cria_modelo(df_preprocessed, df_market, df_ptf)

            # Gerar link da lista de recomendação para baixar
            csv = lista_ids.to_csv(encoding='utf-8')
            b64 = base64.b64encode(csv.encode())
            payload = b64.decode()
            link = "data:text/csv;base64,{payload}"
            link = link.format(payload=payload)

            # Criar botão de download
            return html.Div([html.P(id='mensagem-carregamento', children='Arquivo carregado com sucesso!', style={'margin-top': '10px'}),
                                html.A(html.Button(className='control-download',
                                                    children="Download da lista de recomendacões"),
                                                    href=link,
                                                    download="recomendacoes.csv")],
                                                    style={'text-align': 'center', 'margin-top':'20px'})

    ## Gerar gráfico 1 ----------------------------------------------------------------------------------------------------------------------

    @_app.callback(Output('grafico1', 'figure'),
                  [Input('mensagem-carregamento', 'children')])
    def gerar_grafico1(mensagem):
        if mensagem == 'Arquivo carregado com sucesso!':
            n_recomendacoes = df_sim.shape[0]
            data = [go.Indicator(mode = "number",
                                value = n_recomendacoes,
                                title = {"text": "<span style='color:white'>Nº Total de Recomendações</span>"},
                                domain = {'x': [0, 0], 'y': [0, 0]})]
            layout=go.Layout(paper_bgcolor='#262B3D', plot_bgcolor='#262B3D')
            fig = go.Figure(data=data, layout=layout)

            return fig
        else:
            pass

    ## Gerar gráfico 2 ----------------------------------------------------------------------------------------------------------------------

    @_app.callback(Output('grafico2', 'figure'),
                  [Input('mensagem-carregamento', 'children'),
                  Input('analise-categorica', 'value'),
                  Input('selecao-dataset', 'value')])
    def gerar_grafico1(mensagem, tipo_categorico, tipo_dataset):
        if mensagem == 'Arquivo carregado com sucesso!':
            if tipo_dataset == 'portfolio':
                df = df_treino
            else:
                df = df_sim

            lista = {'de_natureza_juridica':'Natureza jurídica',
                    'de_ramo': 'Ramo de atividade',
                    'de_saude_tributaria': 'Saúde tributária',
                    'de_nivel_atividade': 'Nível de atividade'}
            titulo = lista[tipo_categorico]
            pie_data = Counter(df[tipo_categorico])
            labels = list(pie_data.keys())
            values = list(pie_data.values())

            data=[go.Pie(labels=labels, values=values, hole=.5, showlegend=False, textinfo='none')]
            layout = go.Layout(margin=dict(t=60, b=15, l=50, r=50), paper_bgcolor='#262B3D', plot_bgcolor='#262B3D',
                                title={'text': 'Características do item "{}"'.format(titulo), 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            fig = go.Figure(data=data, layout=layout)
            return fig
        else:
            pass

    ## Gerar gráfico 3 ----------------------------------------------------------------------------------------------------------------------

    @_app.callback(Output('grafico3', 'figure'),
                  [Input('mensagem-carregamento', 'children'),
                  Input('analise-continua', 'value'),
                  Input('selecao-escala', 'value')])
    def gerar_grafico1(mensagem, tipo_continuo, tipo_escala):
        if mensagem == 'Arquivo carregado com sucesso!':
            lista = {'idade_empresa_anos' : 'Idade da empresa (anos)',
            'vl_faturamento_estimado_aux':'Faturamento estimado (R$)',
            'qt_filiais':'Quantidade de filiais (un)'}
            titulo = lista[tipo_continuo]

            # Inserção dos dados
            fig = go.Figure()
            fig.add_trace(go.Histogram(x=df_treino[tipo_continuo], name='Portfolio'))
            fig.add_trace(go.Histogram(x=df_sim[tipo_continuo], name='Recomendacões'))

            # The two histograms are drawn on top of another
            fig.update_layout(barmode='overlay', yaxis_type=tipo_escala, paper_bgcolor='#262B3D', plot_bgcolor='#262B3D',
                            margin=dict(t=50, b=50, l=50, r=0), title={'text': 'Características do item "{}"'.format(titulo),
                                                                'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            fig.update_traces(opacity=0.7)
            return fig
        else:
            pass


## Rodar o app #########################################################################################################################################

# only declare app/server if the file is being run directly
if 'DEMO_STANDALONE' not in os.environ:
    app = run_standalone_app(layout, callbacks, header_colors, __file__)
    server = app.server

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
