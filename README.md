# Portfolio Recommender

**_Web app com Plotly e Dash:_** https://portfoliorecommender.herokuapp.com/

O Portfolio Recommender é o produto final do projeto proposto como conclusão do curso Aceleradev de Data Science da Codenation (Trybe).

## Descrição do desafio

### Objetivo

O objetivo deste produto é fornecer um serviço automatizado que recomenda leads para um usuário dado sua atual lista de clientes (Portfólio).


### Contextualização

Algumas empresas gostariam de saber quem são as demais empresas em um determinado mercado (população) que tem maior probabilidade se tornarem seus próximos clientes. Ou seja, a sua solução deve encontrar no mercado quem são os leads mais aderentes dado as características dos clientes presentes no portfólio do usuário.

Além disso, sua solução deve ser agnóstica ao usuário. Qualquer usuário com uma lista de clientes que queira explorar esse mercado pode extrair valor do serviço.

Para o desafio, deverão ser consideradas as seguintes bases:

Mercado: Base com informações sobre as empresas do Mercado a ser considerado. Portfolio 1: Ids dos clientes da empresa 1 Portfolio 2: Ids dos clientes da empresa 2 Portfolio 3: Ids dos clientes da empresa 3

Obs: todas as empresas(ids) dos portfolios estão contidos no Mercado(base de população).

Link para download das bases Mercado, Portfolio 1, Portfolio 2 e Portfolio 3:

https://drive.google.com/drive/folders/1zQbJsMr81t_y9RYJX3ej1DNb8nPrIeYH?usp=sharing


### Requisitos técnicos obrigatórios do desafio

- Utilizar técnicas de data science e machine learning para desenvolver o projeto;
- Apresentar o desenvolvimento e outputs do modelo em um Jupyter Notebook ou outra tecnologia de apresentação de Output de modelos de Machine Learning;
- A análise deve considerar os seguintes pontos: análise exploratória dos dados, tratamento dos dados, avaliação de algoritmos, treinamento do modelo, avaliação de performance do modelo e visualização dos resultados;
- Para a apresentação do projeto, o tempo entre o treinamento do modelo e o output deve ser menor que 20 min.

## Informação da solução

### *Notebooks relacionados*

- [Análise exploratória e tratamento](https://midoritoyota.github.io/01-AnaliseExploratoriaTratamento.html)
- [Pre processamento](https://midoritoyota.github.io/02-PreProcessamento.html)
- [Criação do modelo](https://midoritoyota.github.io/03-ModeloOneClassSVM.html)
- [Visualização - Buble Chart](https://midoritoyota.github.io/04-Visualiza%C3%A7%C3%A3oDosResultadosBubbleChart.html)
- [Visualização - Heatmap](https://midoritoyota.github.io/05-Visualiza%C3%A7%C3%A3oDosResultadosHeatmap.html)
- [Visualização - Gráficos do App](https://midoritoyota.github.io/06-Visualiza%C3%A7%C3%A3oDosResultados-An%C3%A1lise.html)

### *Web app*

O aplicativo online tem todas as funcionalidades do aplicativo instalado localmente, porém, por limitações de memória do servidor Heroku, o modelo fornece recomendações baseadas em apenas 10% dos dados disponíveis no dataset original.

https://portfoliorecommender.herokuapp.com/

### Como rodar o app localmente

Para instalar o Portfolio Recommender e rodar localmente na sua máquina, siga o passo à passo abaixo:

```bash
# Download do repositório
git clone https://github.com/MidoriToyota/PortfolioRecommender.git

# Instalar os pacotes do requirements.txt
pip install -r requirements.txt

# Rodar o app
python app.py
```

## funcionalidades
