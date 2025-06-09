
import pandas as pd
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
print("dados caregado")
try:
    FileNotFoundError
    

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