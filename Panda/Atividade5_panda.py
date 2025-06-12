
import pandas as pd
#atividade5 analise e exportaçao de dados com pandas
#1.Conte quantos filmes cada diretor dirigiu usando 'Director' Mostre os 5 diretores mais frequentes no dataframe.
#2.Ordene os filmes pelo tempo de duraçao(Runtime) em ordem decrescente e mostre os 10filmes mais longos.
#3.Ordene os filmes por 'Certificate' (ordem alfabeticas) e em seguida, por 'Meta_score' em ordem decrescente. Mosre os 5 primeiros filmes do resultado.
#4. Converta as coluna 'Meta_score' e 'Runtime' para tipo numerico, tratando valores invalidos com errors='coerce'
#5.Agrupe os dados por 'Certificate', calculando:
    #a media de 'Runtime' (tempo de duraçao)
    #a media de 'Meta_score'
    #o total de filmes cerficado
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
"""
#1.Conte quantos filmes cada diretor dirigiu usando 'Director' 
contagem_diretores = df_filmes['Director'].value_counts()
print(contagem_diretores)
#Mostre os 5 diretores mais frequentes no dataframe.
contagem_diretores = df_filmes['Director'].value_counts()
print(contagem_diretores.head(5))
"""
#2.Ordene os filmes pelo tempo de duraçao(Runtime) em ordem decrescente e mostre os 
# 10 filmes mais longos.
#ordenando filmes por mais de uma coluna
#df_ordenado_por_duracao=df_filmes.sort_values(by=['Runtime'],ascending=[False])
#print("\n top 5 filmes por ano e gross:")
#print(df_ordenado_por_duracao.head())

df_filmes['Runtime'] =df_filmes['Runtime'].str.replace('min','')
df_filmes['Runtime']=pd.to_numeric(df_filmes)['Runtime'],errors='coerce')

                                                       

#3.Ordene os filmes por 'Certificate' (ordem alfabeticas) e em seguida, por 'Meta_score'
# em ordem decrescente. Mosre os 5 primeiros filmes do resultado.

df_ordenado_por_certificado=df_filmes.sort_values(by=['Runtime'],ascending=[False])
print("\n top 5 filmes por ano e gross:")
print(df_ordenado_por_certificado.head())



"""
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
