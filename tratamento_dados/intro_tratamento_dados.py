import pandas as pd

df = pd.read_csv('clientes.csv')

# Verificar primeiros registros
print(df.head().to_string())

# Verificar últimos registros
print(df.tail().to_string())

# Verificar qtd de linhas e colunas
print('Quantidade: ', df.shape)

# Verificar tipos de dados
print('Tipagem:\n', df.dtypes)

# Checar valores nulos
print('Valores nulos:\n', df.isnull().sum())
