import pandas as pd

data = {'Nome': ['Alice', 'Anderson', 'Ricardo', 'Pedro', 'Jonas'],
        'Idade': [25, 30, 22, 35, 28],
        'Cidade': ['Maracanaú', 'Pajuçara', 'Montese', 'Mondubim', 'Porangabussu']}

df = pd.DataFrame(data)

# selecionando a coluna "Idade"
coluna_idade = df['Idade']

# filtrando linhas com idade maior que 30
linhas_filtradas = df[df['Idade'] > 30]

# exibindo o resultado
print("Coluna Idade:")
print(coluna_idade)

print("\nLinhas com Idade > 30:")
print(linhas_filtradas)
