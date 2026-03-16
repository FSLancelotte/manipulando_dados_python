import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from scipy.stats import gaussian_kde
from scipy.signal import find_peaks

df = pd.read_csv('ecommerce_estatistica.csv')
LIGHT_TEMPLATE = 'plotly'
# DARK_TEMPLATE = 'plotly_dark'


def criar_histograma(data):
    fig = px.histogram(
        data, x='Nota', nbins=10,
        title='Distribuição de Notas dos Produtos',
        color_discrete_sequence=['skyblue'],
        template=LIGHT_TEMPLATE
    )
    return fig


def criar_dispersao_geral(data):
    fig = px.scatter(
        data, x='Preço', y='Desconto', color='Gênero',
        title='Relação entre Preço e Desconto (Padrão: Masculino)',
        opacity=0.6,
        template=LIGHT_TEMPLATE
    )

    fig.for_each_trace(lambda t: t.update(visible=True if t.name == 'Masculino' else 'legendonly'))

    return fig


def criar_heatmap(data):
    colunas_num = data[['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Qtd_Vendidos_Cod']]
    corr = colunas_num.corr()
    fig = px.imshow(
        corr, text_auto='.2f',
        color_continuous_scale='RdBu_r',
        title='Mapa de Calor: Correlação entre Variáveis',
        template=LIGHT_TEMPLATE
    )
    return fig


def criar_barras_marcas(data):
    top_marcas = data.groupby('Marca')['Qtd_Vendidos_Cod'].sum().nlargest(10).reset_index()
    fig = px.bar(
        top_marcas, x='Marca', y='Qtd_Vendidos_Cod',
        color='Marca', text_auto='.2s',
        title='Top 10 Marcas por Volume de Vendas',
        template=LIGHT_TEMPLATE
    )
    return fig


def criar_pizza_genero(data):
    genero_counts = data['Gênero'].value_counts()
    limite = 0.05
    total = genero_counts.sum()
    mask = (genero_counts / total) < limite

    genero_consolidado = genero_counts[~mask].to_dict()
    if genero_counts[mask].sum() > 0:
        genero_consolidado['Outros'] = genero_counts[mask].sum()

    df_pizza = pd.DataFrame(list(genero_consolidado.items()), columns=['Gênero', 'Quantidade'])

    fig = px.pie(
        df_pizza, values='Quantidade', names='Gênero',
        title='Distribuição de produtos por Gênero',
        hole=0.4,
        template=LIGHT_TEMPLATE
    )
    return fig


def criar_regressao(data):
    fig = px.scatter(
        data, x='Nota', y='Desconto',
        trendline="ols",
        trendline_color_override="red",
        title='Relação entre Desconto e Avaliação (Regressão)',
        template=LIGHT_TEMPLATE
    )
    return fig


def criar_densidade_precos(data):
    precos = data['Preço'].dropna()

    # Cálculo da Densidade
    kde = gaussian_kde(precos)
    x_range = np.linspace(precos.min(), precos.max(), 1000)
    y_densidade = kde(x_range)

    # Picos
    indices_picos, _ = find_peaks(y_densidade, distance=30, height=y_densidade.max() * 0.1)
    valores_picos = x_range[indices_picos]
    alturas_picos = y_densidade[indices_picos]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x_range, y=y_densidade,
        mode='lines', fill='tozeroy',
        name='Densidade', line=dict(color='lightblue', width=3)
    ))

    cores = ['red', 'orange', 'pink', 'purple']
    for i, valor in enumerate(valores_picos):
        cor = cores[i % len(cores)]
        fig.add_vline(x=valor, line_dash="dash", line_color=cor)
        fig.add_annotation(
            x=valor, y=alturas_picos[i],
            text=f"R${valor:.2f}",
            showarrow=True, arrowhead=1, ax=0, ay=-30,
            font=dict(color=cor, size=12)
        )

    fig.update_layout(
        title='Concentração de Preços (Densidade)',
        xaxis_title='Preço (R$)', yaxis_title='Densidade',
        template=LIGHT_TEMPLATE, showlegend=False
    )
    return fig

# --- Dashboard ---

app = dash.Dash(__name__)

app.layout = html.Div(style={'backgroundColor': '#FFFFFF', 'padding': '20px'}, children=[
    html.H1("Dashboard Analítico E-commerce",
            style={'textAlign': 'center', 'color': '#333333', 'fontFamily': 'Arial'}),

    html.Hr(style={'borderColor': '#DDD'}),

    # Linha 1: Histograma e Pizza
    html.Div([
        dcc.Graph(figure=criar_histograma(df), style={'width': '48%'}),
        dcc.Graph(figure=criar_pizza_genero(df), style={'width': '48%'}),
    ], style={'display': 'flex', 'justifyContent': 'space-between'}),

    # Linha 2: Barras e Densidade
    html.Div([
        dcc.Graph(figure=criar_barras_marcas(df), style={'width': '58%'}),
        dcc.Graph(figure=criar_densidade_precos(df)),
    ], style={'display': 'flex', 'justifyContent': 'space-between'}),

    # Linha 3: Dispersão Geral
    html.Div([
        dcc.Graph(figure=criar_dispersao_geral(df))
    ]),

    # Linha 4: Regressão e Heatmap
    html.Div([
        dcc.Graph(figure=criar_regressao(df), style={'width': '48%'}),
        dcc.Graph(figure=criar_heatmap(df), style={'width': '38%'}),
    ], style={'display': 'flex', 'justifyContent': 'space-between'}),
])

if __name__ == '__main__':
    app.run(debug=True)