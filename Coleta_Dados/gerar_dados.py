import pandas as pd
import random
from faker import Faker

faker = Faker('pt-BR')

dados_pessoais = []

for _ in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 60)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime('%d/%m/%Y')
    endereco = faker.address()
    estado = faker.state()
    pais = 'Brasil'

    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'endereco': endereco,
        'estado': estado,
        'pais': pais,
    }

    dados_pessoais.append(pessoa)

df_pessoas = pd.DataFrame(dados_pessoais)
print(df_pessoas)

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)

print(df_pessoas.to_string()) # Usado quando o intuito é apenas printar e não fazer coisas a mais

df_pessoas.to_csv('pessoas.csv')
