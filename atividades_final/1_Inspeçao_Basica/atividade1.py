
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Inspeçao basica do DataFrame
#1. Quantas linhas e colunas tem o nosso DataFrame?
url_filmes = "produtos_mercado.csv"
df_filmes = pd.read_csv(url_filmes)
print("\n informaçoes sobre o dataframe info")
print(df_filmes.info())
#2 Quais são os nomes de todas as colunas?
print(f"\n O dataframe de frutas tem {df_filmes.shape[0]} e colunas {df_filmes.shape[1]}")


#3. Quais são os tipos de dados de cada coluna? A coluna Data_Ultima_Reposicao está no formato
#correto de data?
#index
#tra informaçoes dos indices das linhas
print("\ninformaçoes dos dados: ")
print(df_filmes.dtypes)

#4. Exiba as 7 primeiras linhas do DataFrame.
print("\nprimeiroas 7 linhas do datFrame filmes head: ")
print(df_filmes.head(7))

#5. Exiba as 3 últimas linhas do DataFrame.
df = pd.DataFrame(df_filmes)
ultimas_linhas = df.tail(3)
print(f"\n mostrando as 3 ultimas : {ultimas_linhas}")

#6. Obtenha um resumo estatístico das colunas numéricas (como preço e estoque)
df = pd.DataFrame(df_filmes)
preco_estoque = df[['Preco_Kg', 'Estoque_Kg']].describe()
print(f"\nresumo estatistico = {preco_estoque}")


