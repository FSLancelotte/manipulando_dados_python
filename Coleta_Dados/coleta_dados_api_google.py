import os
try:
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    import io
    from googleapiclient.http import MediaIoBaseDownload
except ImportError:
    print("Erro: O Python ainda não consegue encontrar as bibliotecas.")

SCOPES = ["https://www.googleapis.com/auth/drive.file"]


def enviar_para_drive():
    creds = None

    # CÓDIGO DE AUTENTICAÇÃO
    # Se mudar o SCOPE, precisa deletar o 'token.json' antigo para o Google pedir permissão de escrita!
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("drive", "v3", credentials=creds)

    # Configurações do arquivo
    caminho_local = "C:/Users/fslan/Downloads/produto_informatica_csv.csv"
    metadados = {'name': 'Produto_Informatica_Final.csv'}
    midia = MediaFileUpload(caminho_local, mimetype='text/csv')

    # Execução do POST no Drive
    arquivo = service.files().create(body=metadados, media_body=midia, fields='id').execute()

    print(f"Sucesso! Arquivo enviado. ID no Drive: {arquivo.get('id')}")


enviar_para_drive()


def baixar_arquivo_drive(file_id, nome_saida):

    # Se mudar o SCOPE, precisa deletar o 'token.json' antigo para o Google pedir permissão de escrita!
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("drive", "v3", credentials=creds)

    try:
        # 1. Prepara a requisição de download (GET)
        request = service.files().get_media(fileId=file_id)

        # 2. Cria um buffer na memória para receber os bytes do arquivo
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)

        # 3. Executa o download em partes (chunks)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}%.")

        # 4. Salva o conteúdo do buffer para um arquivo físico no seu computador
        with open(nome_saida, "wb") as f:
            f.write(fh.getvalue())

        print(f"Arquivo '{nome_saida}' baixado com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro no download: {e}")


baixar_arquivo_drive('INSIRA_O_ID_AQUI', 'arquivo_recuperado.csv')
