# Portfolio Recommender
---

Endereço do app: https://portfoliorecommender.herokuapp.com/

O Portfolio Recommender é uma aplicação web que fornece um serviço automatizado de recomendação de leads para um usuário dado sua atual lista de clientes (Portfólio).

Ele foi criado para solucionar o problema de empresas que gostariam de saber quem são as demais empresas em um determinado mercado (população) que tem maior probabilidade de se tornarem seus próximos clientes. Ou seja, quem são os leads mais aderentes dadas as características dos clientes presentes no portfólio do usuário.

Além de retornar uma lista de empresas recomendadas, o Portfolio Recommender também fornece a visualização completa das principais características das empresas do portfolio.

## Codenation (Trybe)

O Portfolio Recommender é o produto final do projeto proposto como conclusão do curso Aceleradev de Data Science da Codenation (Trybe). Os dados foram fornecidos pela Codenation e são todos fictícios.

Link para as bases de dados fornecidas + Descrição das variáveis:

https://drive.google.com/drive/folders/1zQbJsMr81t_y9RYJX3ej1DNb8nPrIeYH?usp=sharing

### Requisitos técnicos obrigatórios do desafio

- Utilizar técnicas de data science e machine learning para desenvolver o projeto;
- Apresentar o desenvolvimento e outputs do modelo em um Jupyter Notebook ou outra tecnologia de apresentação de Output de modelos de Machine Learning;
- A análise deve considerar os seguintes pontos: análise exploratória dos dados, tratamento dos dados, avaliação de algoritmos, treinamento do modelo, avaliação de performance do modelo e visualização dos resultados;
- Para a apresentação do projeto, o tempo entre o treinamento do modelo e o output deve ser menor que 20 min.

## Notebooks relacionados:

[Análise exploratória e tratamento](https://midoritoyota.github.io/01-AnaliseExploratoriaTratamento.html)
[Pre processamento](https://midoritoyota.github.io/02-PreProcessamento.html)
[Criação do modelo](https://midoritoyota.github.io/03-ModeloOneClassSVM.html)
[Visualização - Buble Chart](https://midoritoyota.github.io/04-Visualiza%C3%A7%C3%A3oDosResultadosBubbleChart.html)
[Visualização - Heatmap](https://midoritoyota.github.io/05-Visualiza%C3%A7%C3%A3oDosResultadosHeatmap.html)
[Visualização - Gráficos do App](https://midoritoyota.github.io/06-Visualiza%C3%A7%C3%A3oDosResultados-An%C3%A1lise.html)

## Web app

O link abaixo te leva até o aplicativo online. O aplicativo online tem todas as funcionalidades do aplicativo instalado localmente, porém, por limitação ne memória do servidor Heroku, o modelo fornece recomendações baseadas em apenas 10% dos dados disponíveis no dataset original.

https://portfoliorecommender.herokuapp.com/


## Instalação local

Para instalar localmente siga o passo à passo abaixo:

1. Fazer o download do repositório na sua máquina e executar o comando abaixo no terminal:

```
git clone https://github.com/MidoriToyota/PortfolioRecommender.git
```

Obs: Você pode fazer o download manualmente também clicando em `Code` -> `Download ZIP`

2. Na pasta do arquivo, abrir o terminal e fazer a instalação dos pacotes contidos em `requirements.txt`

```
pip install -r requirements.txt
```

3. Na mesma pasta, rodar o app com o comando:

```
python app.py
```
