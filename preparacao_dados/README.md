# Preparação de Dados
A preparação de dados é o processo de limpar, transformar e organizar dados
brutos para torná-los adequados para análise. É importante porque dados de 
má qualidade podem levar a análises imprecisas e modelos de machine learning
ineficazes. A preparação de dados garante que os dados estejam em um formato
adequado, sem valores nulos ou duplicados, e prontos para serem utilizados em
análises e modelagem.

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
- **transformacao_features.py:**
Estudo da aplicação de técnicas de engenharia de features, como transformação logarítmica,
normalização e contagem de frequência, para melhorar o desempenho dos modelos
analíticos
- **clientes-v2.csv:**
Arquivo base para ser utilização no módulo
- **clientes-v2-tratados:**=
Arquivo com os dados tratados para manipulação posterior. Derivado do 
script *"intro_preparacao_dados.py"*

## Padronização e Normalização
A padronização ajusta os dados para que tenham uma média de 0 e um desvio
padrão de 1, utilizando o método `StandardScaler`. Já a normalização ajusta
os valores para um intervalo específico, geralmente entre 0 e 1, utilizando
o método `MinMaxScaler`. Ambas as técnicas são usadas para trazer os dados 
para uma escala comum, facilitando a comparação e interpretação dos resultados.
