import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('clientes-v3-preparado.csv')

#Uso do Pandas
print('Estatística do dataframe: \n', df.describe())

print('Estatística de um campo: \n ', df[['salario', 'idade']].describe())

print('Correlação: \n', df[['salario', 'idade']].corr())
print('Correlação com Normalização: \n', df[['salarioMinMaxScaler', 'idadeMinMaxScaler']].corr())
print('Correlação com Padronização: \n', df[['salarioStandardScaler', 'idadeStandardScaler']].corr())
print('Correlação com Padronização: \n', df[['salarioRobustScaler', 'idadeRobustScaler']].corr())

print('Correlação: \n', df[['salario', 'idade', 'idadeMinMaxScaler', 'idadeStandardScaler', 'idadeRobustScaler']].corr())

df_filtro_idade = df[df['idade'] < 65]
print('Correlação de clientes menores de 65 anos: \n', df_filtro_idade[['salario', 'idade']].corr())

# Variável espúria - aumenta com o tempo
df['variavel_espuria'] = np.arange(len(df))

print('Variavel_espuria', df['variavel_espuria'].values)

pearson_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod', 'variavel_espuria']].corr()
spearman_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod', 'variavel_espuria']].corr(method='spearman')

print('\nCorrelação de Pearson:\n', pearson_corr)
print('\nCorrelação de Spearman:\n ', spearman_corr)

# Correlações
# Correlação de Pearson e Spearman
# 1.Muito Fraca:
# Valor de Correlação: 0.00 a 0.19
#
# 2.Fraca:
# Valor de Correlação: 0.20 a 0.39
#
# 3.Moderada:
# Valor de Correlação: 0.40 a  0.59
#
# 4.Forte:
# Valor de Correlação: 0.60 a 0.79
#
# 5.Muito Forte:
# Valor de Correlação: 0.80 a 1.00
