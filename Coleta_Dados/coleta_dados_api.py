import requests

def enviar_arquivo():
    caminho = "C:/Users/fslan/Downloads/produto_informatica_csv.csv"

    requisicao = requests.post("https://upload-sa-sao.gofile.io/uploadfile", files={'file': open(caminho,'rb')},timeout=30)
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['data']['downloadPage']
    print("Arquivo enviado. Link para acesso",url)

enviar_arquivo()

# Por conta de problemas de divergência entre o que foi apresentado na aula e a atual operacionalidade do site,
# decidi por mudar o rumo do projeto e trabalhar com a api do google.
