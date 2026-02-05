import pandas
import requests
try:
    from bs4 import BeautifulSoup
    print("Sucesso! BeautifulSoup importado.")
except ImportError:
    print("Erro: O Python ainda não consegue encontrar a biblioteca.")

url = 'https://br.investing.com/indices/bovespa-historical-data'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
print(response.status_code) # Se aparecer 200, deu certo!
print(response.text[:600])


soup = BeautifulSoup(response.text, features="html.parser")
print(soup.prettify()[:1000])

# Utilizando pandas ao invés de buscar diretamente no arquivo de texto do site

print('Pandas: ')
import io

url_dados = pandas.read_html(io.StringIO(response.text))

# Exibe a tabela
print(f"Total de tabelas encontradas: {len(url_dados)}")
print(url_dados[0].head(10))
