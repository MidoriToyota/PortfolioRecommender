import pandas as pd
import numpy as np

df = pd.read_csv('data/df_preprocessed.csv', index_col='id')
df1, df2, df3 = np.array_split(df, 3)

df1_preprocessed = pd.DataFrame(df1)
df2_preprocessed = pd.DataFrame(df2)
df3_preprocessed = pd.DataFrame(df3)

df1_preprocessed.to_csv("data/df1_preprocessed.csv", index=True)
df2_preprocessed.to_csv("data/df2_preprocessed.csv", index=True)
df3_preprocessed.to_csv("data/df3_preprocessed.csv", index=True)
