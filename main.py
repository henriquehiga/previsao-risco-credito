import pandas as pd

# Dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data'

# Nomes de coluna conforme doc: https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data
colunas = [
    'status_conta_corrente', 'duracao_mes', 'historico_credito', 'proposito',
    'valor_credito', 'poupanca', 'tempo_emprego_atual', 'taxa_prestacao',
    'estado_civil_sexo', 'outros_devedores', 'residencia_desde', 'propriedade',
    'idade', 'outros_planos_pagamento', 'habitacao', 'num_creditos_existentes',
    'emprego', 'num_dependentes', 'telefone', 'trabalhador_estrangeiro', 'risco'
]

df_credito = pd.read_csv(url, sep=' ', header=None, names=colunas)

# Pré-processamento para que o modelo compreenda categorias qualitativas utilizando Label Encoding;

# Utilizei label encoding pois este campo possui informação ordinal. Considerando que 5 é bom e 1 é ruim, fiz o mapeamento abaixo:
# para que a coluna historico_credito não seja inputada no modelo como sendo uma identificação externa, mas um valor lógico
df_credito['historico_credito'] = df_credito['historico_credito'].map({'A30': 5, 'A31': 4, 'A32': 3, 'A33': 2, 'A34': 1})

print(df_credito.tail(10))