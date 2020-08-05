import base64
import os

import dash
import dash_core_components as dcc
import dash_html_components as html

## Função 1 ######################################################################################

""" Função que roda o app como um app autonomo
    Cria o esqueleto funcional do app."""

def run_standalone_app(
        layout,
        callbacks,
        header_colors,
        filename):

    # Criar objeto "app" e definir algumas configurações
    app = dash.Dash(__name__)
    app.scripts.config.serve_locally = True
    app.config['suppress_callback_exceptions'] = True

    # Setar nome do app e título
    app_name = 'Portfolio Recommender'
    app_title = 'Portfolio Recommender'

    # Pega a função definida abaixo (app_page_layout) e roda
    app.layout = app_page_layout(
        page_layout=layout(),
        app_title=app_title,
        app_name=app_name,
        standalone=True,
        **header_colors())

    # Register all callbacks
    callbacks(app)

    # return app object
    return app

## Função 2 ######################################################################################

""" Função que cria o cabeçalho do app.
    Apenas a parte de cima que tem o nome do app
    e o link do github."""

def app_page_layout(page_layout,
                    app_title="Dash Bio App",
                    app_name="",
                    light_logo=True,
                    standalone=False,
                    bg_color="#506784",
                    font_color="#F3F6FA"):

    return html.Div(
        id='main_page',
        children=[
            dcc.Location(id='url', refresh=False),
            html.Div(
                id='app-page-header',
                children=[
                    html.H2(app_title, style={'font-family': 'Arial', 'padding-left':'20px'}),

                    html.A(
                        id='gh-link',
                        children=['Ver no Github'],
                        href="https://github.com/MidoriToyota/RecommenderWebApp",
                        style={'color': 'white' if light_logo else 'black',
                               'border': 'solid 1px white' if light_logo else 'solid 1px black'})],

                style={'background': bg_color,
                       'color': font_color}),

            html.Div(
                id='app-page-content',
                children=page_layout
            )
        ],
    )
