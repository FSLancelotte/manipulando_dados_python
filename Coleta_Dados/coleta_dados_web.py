import requests
from pyexpat import features

try:
    from bs4 import BeautifulSoup
    print("Sucesso! BeautifulSoup importado.")
except ImportError:
    print("Erro: O Python ainda não consegue encontrar a biblioteca.")

url = 'https://python.org.br/web/'
req = requests.get(url)
extracao = BeautifulSoup(req.text, features='html.parser')

# Exibir o texto
# print(extracao.text.strip())

# contagem_titulo = 0
# contagem_linha = 0
# # Filtrar a exibição pela tag
# for linha_texto in extracao.find_all(['h2', 'p']):
#     if linha_texto.name == 'h2':
#         titulo = linha_texto.text.strip()
#         print('Título: \n', titulo)
#         contagem_titulo += 1
#     elif linha_texto.name == 'p':
#         linha = linha_texto.text.strip()
#         print(linha)
#         contagem_linha += 1
#
#
# print('Contagem titulo: ', contagem_titulo)
# print('Contagem linha: ', contagem_linha)

# Exibir tags Aninhadas
for titulo in extracao.find_all('h2'):
    print('Título: ', titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
        for a in link.find_all('a', href=True):
            print('Texto Link: ', a.text.strip(), ' | URL:', a['href'])
