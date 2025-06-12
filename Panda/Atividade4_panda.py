
import pandas as pd
#atividade4
#1. verifique quantos valores ausentes existem nas colunas 'Revenue(Millions) e 'Metascore'do df_filmes original.
#2. crie um novo DataFrame chamado df_filmes_completo removendo todas as linhas que tenham qualquer vaor ausente.
#   Quantas linhas restaram?
#3 Crie outroDataFrame chamado df_filmes_preenchido_media Nele, preecha os valores ausentes de 
# 'Revenue (Millions)' com a media dessa coluna e os valores ausentes de 'Metascore' 
# com a mediana dessa coluna. Veriique se ainda ha NaNs nessas colunas

url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
#1. verifique quantos valores ausentes existem nas colunas 'Revenue(Millions) e 
# 'Metascore'do df_filmes original.
#verificar dados ausents com  .isna() .sem():
#print('\n Contagem de valores ausentes por coluna:')

# Verificando valores ausentes nas colunas especificadas
#df_filmes[['Revenue(Millions)', 'Metascore']].isnull().sum()
#print(df_filmes.isna().sum())
print("Valores ausentes por coluna:")
print(df_filmes[['Gross','Meta_score']].isna().sum())

df_filmes_completo =df_filmes.dropna()
print(f"\nNumeros de linahs DataFrame origianl:{len(df_filmes)}")
print(f"Numero de linhas apos remover todas com NaN:{len(df_filmes_completo)}")
#Garantiddo as colunas estão numericas
df_filmes['Gross']=pd.to_numeric(df_filmes['Gross'],errors='coerce')
df_filmes['Meta_score']=pd.to_numeric(df_filmes['Meta_score'],errors='coerce')
#criandouma copia do DataFrame original
df_filmes_preechido_media= df_filmes.copy()

#preenchend NaNs
df_filmes_preechido_media['Gross']=df_filmes_preechido_media['Gross'].fillna
(df_filmes_preechido_media['Gross'].mean())
df_filmes_preechido_media['Meta_score']=df_filmes_preechido_media
['Meta_score'].fillna(df_filmes_preechido_media['Meta_score'].median())
#verifacndo se ainda existem NaNis nessas colunas
print("\nValores ausentes apos preenchimentos:")
print(df_filmes_preechido_media[['Gross','Meta_score']].isna())


"""
#verificar dados ausents com  .isna() .sem():
print('\n Contagem de valores ausentes por coluna:')
print(df_filmes.isna().sum())

#Removendo linhas/colunas
#Criando uma copia para não
df_sem_nan_linhas= df_filmes.copy()
#Removnedo todaas linhas que contenham qualquer valor nan
#inplace : altera arquivo original
df_sem_nan_linhas.dropna(inplace=True)
print(f"\n numero de linahs origianl: {len(df_filmes)}")
print(f"\n numero de linhas opos drog: {len(df_sem_nan_linhas)}")

#removendo colunas que tenham qualquer valor Nan
df_sem_nan_colunas = df_filmes.dropna(axis=1) #axis 1 deleta colunas axis e 0 deleta linhas
print(f"Colunas originais: {df_filmes.columns.tolist()}")
print(f"Colunas apos dropna: {df_sem_nan_colunas.columns.tolist()}")
"""
