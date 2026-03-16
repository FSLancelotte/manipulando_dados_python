# Exercício do módulo 23

## Enunciado do exercício
Leia o arquivo ‘ecommerce_estatistica.csv’ dentro de um dataframe;

Crie uma aplicação Dash para visualizar os gráficos do módulo anterior;

## O que foi feito:
O código foi modularizado em funções responsáveis por criar os gráficos.
Seguiu-se o que havia sido feito no exercício do módulo anterior, migrando para
as bibliotecas Dash e Plotly para a criação de uma aplicação interativa.
A aplicação Dash é executada num localhost, podendo ser acessada pelo navegador.

Como é possível o próprio usuário criar um filtro, o gráfico de dispersão que filtrava
apenas produtos do gênero masculino foi removido, ficando o gráfico de dispersão que
engloba todos os produtos. Este gráfico como padrão aparece para o usuário com apenas
os produtos masculinos selecionados, mas é possível selecionar o filtro desejado na aplicação.