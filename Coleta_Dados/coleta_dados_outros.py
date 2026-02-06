import pymysql
import pandas as pd
from sqlalchemy import create_engine

def conexao_mysql(host, user, password, db, table):

    conn = pymysql.connect(host=host, port=3306, user=user, password=password, db=db)

    cursor = conn.cursor()

    # Executar consulta
    query = f"SELECT * from {table} LIMIT 10"
    cursor.execute(query)

    # Buscar resultados
    resultados = cursor.fetchall()

    # Exibir os resultados
    print('Tabela MySQL:')
    for linha in resultados:
        print(linha)

    # Fechar conexão
    cursor.close()
    conn.close()

def df_conexao_mysql(host, user, password, db, table):

    conn = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{db}')

    query = f"SELECT * FROM {table}"
    df = pd.read_sql_query(query, conn)

    # Exibir resultados
    print('Tabela MySQL com DataFrame: \n', df.head())

    #Fechar a conexão
    conn.dispose()
    return df

def conexao_xlsx(path):
    # Ler arquivo Excel
    df = pd.read_excel(path)
    print('Tabela Excel: \n', df.head())

    # Escrever arquivo CSV
    df.to_csv('dados.csv', index=False)


def conexao_csv(path):
    # Ler arquivo csv
    df = pd.read_csv(path)
    print('Tabela CSV: \n', df.head())

    # Escrever arquivo CSV
    df.to_json('dados.json', index=False)


# conexao_mysql(host='localhost', user='root', password='root', db='loja_informatica', table='cliente')
df_cliente = df_conexao_mysql(host='localhost', user='root', password='root', db='loja_informatica', table='cliente')
df_cliente.to_excel(excel_writer='dados.xlsx', index=False)

conexao_xlsx('dados.xlsx')
conexao_csv('dados.csv')