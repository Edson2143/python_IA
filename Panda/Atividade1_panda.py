
import pandas as pd
#atividade explorando o dataframe de filmes
#1. Carregue o Dataframe df_filmes como mostrado acima
#2. use .head() para ver as primeiras 7 linhas
#3. use .info() para entender os tipos de dados e valores nulos. quantas colunas tem valores ausentes?
#4. quantos filmes (linhas) e caracteristicas (colunas) existemte no dataset? use .shape
#5. ise .describe() para aas estatisticas de colua "rating" qual a nota media dos filmes?



url_filmes = "netflix_titles.csv"
df_filmes = pd.read_csv(url_filmes)
print(f"dados caregado : {url_filmes}")
#print(f"dados caregado : {df_filmes}")
print("primeiroas 7 linhas do datFrame filmes head: ")
print(df_filmes.head(7))

#info
print("\n informaçoes sobre o dataframe info")
print(df_filmes.info())
print(f"\n O dataframe de filmes tem {df_filmes.shape[0]} e colunad {df_filmes.shape[1]}")

#Describe
#Gera estatistica dodataframe
print("estatistica descritiva do dataframe: ")
print(df_filmes.describe())

"""
#primeiros comados
#Head() eo Tail()
print("primeiroas 5 linhas do datFrame filmes head: ")
print(df_filmes.head())
#Tail
print("\n Ultimas 5 linhas Tail")
print(df_filmes.tail())
#info
print("\n informaçoes sobre o dataframe info")
print(df_filmes.info())

print(f"\n O dataframe de filmes tem {df_filmes.shape[0]} e colunad {df_filmes.shape[1]}")

#Describe
#Gera estatistica dodataframe
print("estatistica descritiva do dataframe: ")
print(df_filmes.describe())

#index
#tra informaçoes dos indices das linhas
print("iformaçoes do incice: ")
print (df_filmes.index)
"""