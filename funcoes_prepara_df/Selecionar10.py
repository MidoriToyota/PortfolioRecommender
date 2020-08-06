import pandas as pd
import numpy as np

df = pd.read_csv('df_preprocessed.csv', index_col='id' )
df1 = pd.read_csv('estaticos_portfolio1.csv')
df2 = pd.read_csv('estaticos_portfolio2.csv')
df3 = pd.read_csv('estaticos_portfolio3.csv')

df11 = df[df.index.isin(df1.id)]
df22 = df[df.index.isin(df2.id)]
df33 = df[df.index.isin(df3.id)]
frame = [df11, df22, df33]

# Apenas empresas que pertencem aos portfolios
df_portfolio = pd.concat(frame)

# Somente empresas que não pertencem aos portfolios
pertence = df.index.isin(df_portfolio.index)
nao_pertence = [not i for i in pertence]
df_nao_pertence = df[nao_pertence]

# 10% das empresas que pertencem ao portfolio
d1, d2, d3, d4, d5, d6, d7, d8, d9, d10 = np.array_split(df_nao_pertence, 10)

# Juntar os dados do portfolio e os 10% de mercado fora do portfolio
df_preprocessed10 = pd.concat([df_portfolio, d1])

# Escrever um csv
df_preprocessed10.to_csv('df_preprocessed10.csv', index=True)

# Selecionar as mesmas linhas do dataset df_market

df = pd.read_csv('df_preprocessed.csv', index_col='id' )
df_market = pd.read_csv('df_market.csv', index_col='id' )
df_market10 = df_market[df_market.index.isin(df.index)]
df_market10.to_csv('df_market10.csv', index=True)
