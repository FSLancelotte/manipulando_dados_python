# Tratamento de dados

## Explicação dos arquivos presentes nesta pasta
- **intro_tratamento_dados.py:** Script da aula introdutória ao tratamento
de dados. Demonstra alguns métodos para entender os dados de um arquivo
- **estudo_lambda.py:** Script criado com o objetivo de explorar o uso da
função lambda e comparar seu uso com o uso de uma função própria
- **limpeza_dados.py:** Script voltado para o estudo de técnicas de limpeza de
dados. Trabalha exclusões de linhas com valores nulos ou repetidos, bem como
a alteração de dados para normalização.
- **outliers.py:** Script que explora técnicas para tratar dados que estão
discrepantes na amostra (muito menor ou maior que os outros). Os outliers
podem ser prejudiciais no momento da análise dos dados, contaminando as
informações. Os dois métodos principais utilizados foram o Z-score e o IQR.
- **clientes.csv:** Lista de dados de clientes fictícios, 
utilizada para estudo
- **clientes_limpeza.csv:** Lista de dados de clientes fictícios gerada após 
o tratamento de dados no script *"limpeza_dados.py"*

## Z-score vs IQR
O Z-Score mede quantos desvios padrões um ponto está da média, enquanto o 
IQR foca na posição dos dados (mediana) em vez da média usando
os quartis (25% e 75%).

O Z-score deve ser usado quando os dados seguirem uma distribuição normal. 
O IQR lida melhor com dados que não seguem uma distribuição normal ou dados 
que possuem muitos outliers que podem distorcer a média.

