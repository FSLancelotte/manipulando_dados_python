# Preparação de Dados

## Explicação dos arquivos presentes nesta pasta

- **intro_preparacao_dados.py:**
Script de introdução ao módulo, voltado para entender o comportamento
dos dados e prepará-los para manipulação, removendo dados sensíveis.
- **normalizacao_padronizacao.py:**
Script que aborda métodos de normalização e padronização através de 
funções da biblioteca ***sklearn***: 
  - MinMaxScaler: Normaliza os dados entre valores 0 e 1 ou -1 e 1;
  - StandardScaler: Padroniza os dados com base no Z-score, tendo foco
  na média em torno de 0 e o desvio padrão em torno de 1;
  - RobustScaler: Padroniza os dados com base no IQR com foco em Mediana
  e interquartis, sendo robusto a outliers
- **codificacao_variaveis_categoricas.py:**
Voltado para a transformação de variáveis categóricas em variáveis numéricas
para uso posterior em análises estatísticas e no uso de IA (machine learning)
- **clientes-v2.csv:**
Arquivo base para ser utilização no módulo
- **clientes-v2-tratados:**
Arquivo com os dados tratados para manipulação posterior. Derivado do 
script *"intro_preparacao_dados.py"*