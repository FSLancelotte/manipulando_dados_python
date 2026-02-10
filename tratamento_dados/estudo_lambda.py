import pandas as pd

# Função para calcular o cubo de um número

def eleva_cubo(x):
    return x ** 3

# Expressão de lambda para calcular o cubo de um número
eleva_cubo_lambda = lambda x : x ** 3 # Não deve ser usado desta forma, isto é apenas para entender de forma didática

print(eleva_cubo_lambda(5))
print(eleva_cubo_lambda(5))

df = pd.DataFrame({'numeros': [1, 2, 3, 4, 5, 10]})

df['cubo_funcao'] = df['numeros'].apply(eleva_cubo)
df['cubo_lambda'] = df['numeros'].apply(lambda x: x ** 3) # Uso correto da função lambda
print(df)

# Para manipulações e cálculos complexos o uso de uma função é mais recomendado
# Para uma simples operação matemática o uso da função lambda pode simplificar e economizar linhas de código