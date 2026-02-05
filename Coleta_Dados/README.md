# Coleta de dados
Foram utilizados métodos de web scraping e pandas. Ao avançar no módulo houve
uma divergência entre comportamento do site apresentado com sua a atual
implementação, o que impediu seguir exatamente como executado na aula.

Essa divergência fez com que este projeto incorporasse uma api mais estável e
profissional como a do Google. Foi criada então uma integração com a api do
Google Drive capaz de enviar um arquivo para o Drive e baixá-lo em seguida
através da ID gerada no envio.

### Explicação dos arquivos presentes nesta pasta
> - **coleta_dados_basica.py:**
> Script feito para introduzir noções de ***web scraping*** e utilização do
pacote ***pandas***.

> - **coleta_dados_web.py:**
> Aprofundando o *web scraping* com o uso de tags

> - **coleta_dados_api.py:**
> Utilização de api para enviar e baixar arquivos através de métodos *POST* e *GET*

> - **coleta_dados_api_google.py**
> Utilização da api do google para fazer a tarefa de enviar e baixar aquivos,
> uma vez que o site referenciado na aula não permitia esta tarefa

> - **quickstart.py**
> Arquivo de exemplo cedido pela documentação do google workspace para a 
> execução da API

> - **produto_informatica.csv e arquivo_recuperado.csv:**
> São os arquivo utilizados para envio e recuperação
> através da execução do script **coleta_dados_api_google.py**

### Sobre a API do Google
Para o projeto funcionar, é necessário conectar o aplicativo com um projeto
no google workspace. Após criar um projeto no workspace, configurá-lo e adicionar
usuários permitidos para teste, **é necessário baixar um arquivo json de
um cliente configurado no projeto**. Este arquivo json vem com um nome como 
"cliente_secret_STRING_STRING.json" e **é preciso renomeá-lo para "credentials.json"**.
Por motivos de segurança esses arquivos foram adicionados ao .gitignore e não
estão disponíveis no repositório.
