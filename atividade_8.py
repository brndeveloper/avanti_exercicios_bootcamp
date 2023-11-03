import pandas as pd
import numpy as np

# criando um DataFrame genérico com valores ausentes
data = {'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 2, 3, np.nan, 5],
        'C': [1, 2, 3, 4, 5]}

df = pd.DataFrame(data)

# verificando valores ausentes
print("Valores ausentes no DataFrame:")
print(df.isna())

# pode-se preencher valores ausentes com um valor específico, nesse caso o 0 foi o escolhido
df_filled = df.fillna(0)
print("\nDataFrame com valores ausentes preenchidos:")
print(df_filled)

# removendo linhas com valores ausentes
df_dropped = df.dropna()
print("\nDataFrame com linhas contendo valores ausentes removidas:")
print(df_dropped)