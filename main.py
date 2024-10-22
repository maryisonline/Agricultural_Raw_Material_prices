# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("kianwee/agricultural-raw-material-prices-19902020")

# print("Path to dataset files:", path)

import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\mary saotome\Desktop\projetos\Back-end\kagglehub\datasets\kianwee\agricultural-raw-material-prices-19902020\versions\1\agricultural_raw_material.csv')
# print(df.head())
df.info() # mostra as principais informacoes do dataframe
# df.isnull().sum()


# TRATATIVA DO DATASET

# dando replace para %, , e -
df = df.replace('%', '', regex=True)
df = df.replace(',', '', regex=True)
df = df.replace('-', '', regex=True)
df = df.replace('MAY0', np.nan)
df = df.replace('', np.nan)
df = df.dropna() # atualiza o dataframe
# df.isnull().sum()


df.Month = pd.to_datetime(df.Month.str.upper(), format='%b%y', yearfirst=False)
df = df.set_index('Month') # definindo como indice

print(df.head())

# INICIO DA ANALISE

import seaborn as sbn
import matplotlib as mpl
from matplotlib import pyplot as plt

# estilizacao do grafico
sbn.set_style('darkgrid')
mpl.rcParams['font.size'] = 14
mpl.rcParams['figure.figsize'] = (9, 5)
mpl.rcParams['figure.facecolor'] = '#00000000'

# dados do grafico
# lista dos materias
raw_data = ['Coarse wool Price', 'Copra Price', 'Soft sawnwood Price', 'Wood pulp Price', 'Cotton Price', 'Fine wool Price', 'Hard log Price',
            'Hard sawnwood Price', 'Hide Price', 'Plywood Price', 'Rubber Price', 'Softlog Price', 'Wood pulp Price']

corrmat = df[raw_data].corr()

fig = plt.figure(figsize= (12, 9))

mask = np.triu(np.ones_like(corrmat, dtype=bool))
sbn.heatmap(corrmat, vmax= .8, mask=mask, square= True, annot= True)

plt.show()
