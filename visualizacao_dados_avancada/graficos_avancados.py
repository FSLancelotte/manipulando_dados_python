import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc


def cria_graficos(df): # O ideal é criar uma função por gráfico
    # Histograma
    fig1 = px.histogram(df, x='salario', nbins=30, title='Distribuição de Salários')

    fig2 = px.pie(df, names='area_atuacao', color='area_atuacao', color_discrete_sequence=px.colors.sequential.RdBu)

    # Gráfico de bolhas
    fig3 = px.scatter(df, x='idade', y='salario', size='anos_experiencia', color='area_atuacao', hover_name='estado', size_max=60)
    fig3.update_layout(title='Salário por Idade e Anos de Experiência')

    # Gráfico de Linha
    fig4 = px.line(df, x='idade', y='salario', color='area_atuacao', facet_col='nivel_educacao')
    fig4.update_layout(
        title='Salário por Idade e Área de Atuação para cada Nível de Educação',
        xaxis_title='Idade',
        yaxis_title='Salário'
    )

    # Gráfico 3D
    fig5 = px.scatter_3d(df, x='idade', y='salario', z='anos_experiencia', color='nivel_educacao')

    # Gráfico de Barra
    fig6 = px.bar(df, x='estado_civil', y='salario', color='nivel_educacao', barmode='group', color_discrete_sequence=px.colors.sequential.RdBu, opacity=1)
    fig6.update_layout(
        title='Salário por Estado Civil e Nível de Educação',
        xaxis_title='Estado Civil',
        yaxis_title='Salário',
        legend_title='Nível de Educação',
        plot_bgcolor='rgb(222, 255, 253, 1)', # Fundo interno
        paper_bgcolor='rgb(186, 245, 241, 1)' # Fundo externo
    )
    return fig1, fig2, fig3, fig4, fig5, fig6

def cria_app(df):
    # Cria app
    app = Dash(__name__)

    fig1, fig2, fig3, fig4, fig5, fig6 = cria_graficos(df)

    app.layout = html.Div(children=[
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6)
    ])
    return app


df = pd.read_csv('clientes-v3-preparado.csv')

if __name__ == '__main__':
    app = cria_app(df)
    app.run(debug=True, port=8050)