import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

df = pd.read_csv('ecommerce_estatistica.csv')
print(df.head().to_string())

# --- 1. GRÁFICO DE HISTOGRAMA ---
# Objetivo: Analisar a distribuição das avaliações (Notas)
plt.figure()
sns.histplot(data=df, x='Nota', bins=10, kde=False, color='skyblue')
plt.title('Distribuição de Notas dos Produtos', fontsize=18)
plt.xlabel('Nota (Avaliação)')
plt.ylabel('Frequência de Produtos')
plt.savefig('histograma_distribuicao_notas.png')
plt.show()

# --- 2. GRÁFICO DE DISPERSÃO GERAL ---
# Objetivo: Ver a relação entre Preço e Desconto
plt.figure(figsize=(12, 7))

sns.scatterplot(
    data=df,
    x='Preço',
    y='Desconto',
    hue='Gênero',
    s=40,       # Ajuste de tamanho dos pontos
    alpha=0.6,
    palette='Set2'
)

plt.title('Relação entre Preço e Desconto por Gênero', fontsize=20, pad=20)
plt.xlabel('Preço (R$)', fontsize=16)
plt.ylabel('Desconto (%)', fontsize=16)

# Ajuste da legenda para fora do gráfico
plt.legend(
    title='Gênero',
    bbox_to_anchor=(1.02, 1),
    loc='upper left',
    borderaxespad=0.
)

plt.tight_layout()
plt.savefig('dispercao_preco_desconto_geral.png')
plt.show()

# --- 2. GRÁFICO DE DISPERSÃO COM FILTRO ---
# Objetivo: Ver a relação entre Preço e Desconto nos produtos Masculinos
plt.figure(figsize=(12, 7))

# Criando um df apenas para o gênero Masculino
df_filtro = df[df['Gênero'] == 'Masculino']

sns.scatterplot(
    data=df_filtro,
    x='Preço',
    y='Desconto',
    s=80,          # Tamanho reduzido dos pontos
    alpha=0.6,     # Transparência para lidar com sobreposição
)

plt.title('Relação entre Preço e Desconto dos produtos Masculinos', fontsize=20, pad=20)
plt.xlabel('Preço (R$)', fontsize=16)
plt.ylabel('Desconto (%)', fontsize=16)

plt.tight_layout()
plt.savefig('dispercao_preco_desconto_masculino.png')
plt.show()


# --- 3. MAPA DE CALOR (HEATMAP) ---
# Objetivo: Identificar correlações entre variáveis numéricas
plt.figure(figsize=(12, 8))
colunas_num = df[['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Qtd_Vendidos_Cod']]
corr = colunas_num.corr()
heatmap = sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap='coolwarm',
    annot_kws={"size": 14, "weight": "bold"},
    cbar_kws={'label': 'Escala de Correlação'} # Adiciona um título à barra lateral
)
plt.title('Correlação entre Variáveis', fontsize=18)
plt.xticks(fontsize=12, rotation=0)
plt.yticks(fontsize=12, rotation=0)
cbar = heatmap.collections[0].colorbar
cbar.ax.tick_params(labelsize=12)
cbar.set_label('Correlação', size=14)
plt.tight_layout()
plt.savefig('heatmap_variaveis_numericas.png')
plt.show()

# --- 4. GRÁFICO DE BARRA ---
# Objetivo: Comparar a quantidade vendida pelas top 10 marcas
plt.figure()
top_marcas = df.groupby('Marca')['Qtd_Vendidos_Cod'].sum().nlargest(10).reset_index()
barras = sns.barplot(data=top_marcas, x='Marca', y='Qtd_Vendidos_Cod', hue='Marca', legend=False)

for container in barras.containers:
    barras.bar_label(container, padding=2, fontsize=8, fontweight='bold', rotation=10)

plt.title('Top 10 Marcas por Volume de Vendas', fontsize=18)
plt.xlabel('Marca', fontsize=16)
plt.ylabel('Total de Vendas', fontsize=16)
plt.xticks(rotation=25)

plt.ylim(0, top_marcas['Qtd_Vendidos_Cod'].max() * 1.1)
plt.tight_layout()
plt.savefig('barras_marcas_vendidas.png')
plt.show()

# --- 5. GRÁFICO DE PIZZA ---
# Objetivo: Mostrar a proporção de produtos por Gênero
genero_counts = df['Gênero'].value_counts()

# Filtrar Gêneros menos representativos
limite = 0.05
total = genero_counts.sum()
mask = (genero_counts / total) < limite
outros_total = genero_counts[mask].sum()

genero_consolidado = genero_counts[~mask]
if outros_total > 0:
    genero_consolidado['Outros'] = outros_total


plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(
    genero_consolidado,
    labels=genero_consolidado.index,
    autopct='%1.1f%%',
    startangle=140,
    textprops={'fontsize': 16}, # Aumenta a fonte dos nomes das fatias
    pctdistance=0.85            # Ajusta a distância da porcentagem ao centro
)

plt.title('Distribuição de produtos por Gênero', fontsize=18)
plt.tight_layout()
plt.savefig('pizza_genero_percentual_vendas.png')
plt.show()

# --- 6. GRÁFICO DE DENSIDADE ---
# Objetivo: Entender a concentração de preços
plt.figure()
kde = sns.kdeplot(data=df, x='Preço', fill=True, color='lightblue')

if not kde.lines:
    sns.kdeplot(data=df, x='Preço', ax=kde, fill=False, color='none')

# Identificar picos
x_data, y_data = kde.lines[0].get_data()
indices_picos, _ = find_peaks(y_data, distance=30, height=0.001)
valores_picos = x_data[indices_picos]
alturas_picos = y_data[indices_picos]
cores = ['red', 'orange', 'pink', 'purple']

for i, valor in enumerate(valores_picos):
    cor = cores[i % len(cores)]
    plt.axvline(valor, color=cor, linestyle='dashed', alpha=0.7, label=f'Pico {i+1}: R${valor:.2f}')
    plt.text(valor, alturas_picos[i], f'R${valor:.2f}', color=cor, fontweight='bold', ha='center', va='bottom')

plt.title('Concentração de Preços', fontsize=16)
plt.xlabel('Preço (R$)')
plt.ylabel('Densidade')
plt.savefig('densidade_precos.png')
plt.show()

# --- 7. GRÁFICO DE REGRESSÃO ---
# Objetivo: Verificar se descontos resultam em uma melhor avaliação
plt.figure()
sns.regplot(data=df, x='Nota', y='Desconto', scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
plt.title('Relação entre Desconto e Avaliação', fontsize=14)
plt.xlabel('Avaliação do Produto')
plt.ylabel('% de Desconto')
plt.savefig('regressao_avaliacao_desconto.png')
plt.show()