# exemplo de leitura de um arquivo CSV em um DataFrame, em seguida uma exibição das primeiras linhas
import pandas as pd

dataframe = pd.read_csv('caminho_do_arquivo.csv')

print(dataframe.head()) # exibindo através do print