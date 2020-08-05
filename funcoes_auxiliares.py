# Pacotes ------------------------------------------------------------------------------------------------------------------------------
from sklearn.svm import OneClassSVM
import pandas as pd
import numpy as np
import base64
import io
from io import BytesIO
import os
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


# Função para criar o modelo -------------------------------------------------------------------------------------------------------------

def cria_modelo(df_preprocessed, df_market, df_ptf):

    # Dados de treino e dados de validação
    df_train = df_preprocessed[df_preprocessed.index.isin(df_ptf.id)]

    # Treinamento do modelo
    clf = OneClassSVM(gamma='auto').fit(df_train)

    # Calcular treshold
    score_train = clf.score_samples(df_train)
    treshold = np.quantile(score_train, 0.1)

    # Aplicar modelo nos dados de mercado
    score_test = clf.score_samples(df_preprocessed)

    # Classificação utilizando o treshold
    pred = score_test>=treshold

    # Criação de coluna "recomendado" com os labels
    portfolio = df_market.index.isin(df_ptf.id)
    df_market_labeled = df_market.copy()
    aux = ['Sim' if n==True else 'Não' for n in pred]
    label = ['Treino' if portfolio[n]==True else aux[n] for n in range(len(portfolio))]
    df_market_labeled.insert(8, 'recomendado', label)
    df_market_labeled.insert(9, 'contador', 1)

    df_treino = df_market_labeled[df_market_labeled['recomendado']=='Treino']
    df_sim = df_market_labeled[df_market_labeled['recomendado']=='Sim']
    lista_ids = pd.DataFrame(df_sim.index)

    return df_treino, df_sim, lista_ids


# Função Ler arquivo CSV do usuário -------------------------------------------------------------------------------------------------------------

def parse_contents(contents, filename):

    # Recebe o conteúdo e decodifica
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    # Usa a função certa para os arquivos legíveis
    try:
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            df = pd.read_excel(io.BytesIO(decoded))

    except Exception as e:
        print(e)
        return html.Div([
            'Ocorreu um erro no processamento dos dados. Atualize a página e tente novamente.'
        ])
    return df
