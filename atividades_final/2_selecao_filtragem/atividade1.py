
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Seleção e Filtragem de Dados:
#1. Selecione e exiba apenas a coluna 'Produto'.
url_filmes = "produtos_mercado.csv"
df_filmes = pd.read_csv(url_filmes)
#7. Selecione e exiba apenas a coluna 'Produto'
fruta_selecionados = df_filmes[['Produto']]
print (f"\nDataframe com protudo")
print(fruta_selecionados.head())

#8. Selecione e exiba as colunas 'Produto', 'Categoria' e 'Preco_Kg'
fruta_selecionados = df_filmes[['Produto','Categoria','Preco_Kg']]
print (f"\nDataframe com protudo")
print(fruta_selecionados.head())

#9.Exiba os dados do produto com ID_Produto igual a 110 (Limão Tahiti) 
selecao_especifica = df_filmes.iloc[[110]]#,[1,4]]
print("\n Printando uma seleçao especifica, ID_produto 110")
print(selecao_especifica)

#10. Quais são os produtos da categoria 'Verdura'?
verdura = df_filmes[df_filmes["Categoria"].str.contains("Verdura",na=False)]
print("\n categoria legumes'")
print(verdura[['Categoria']])

#11. Quais frutas têm um Preco_Kg superior a R$ 10,00?
preco_superior = df_filmes[df_filmes["Preco_Kg"]>=10.00]
print("\nProduto com preço >= 10.00:")
print(preco_superior['Preco_Kg'])

#12. Quais produtos foram repostos no dia '2024-06-01'?
data_reposto = df_filmes[df_filmes["Data_Ultima_Reposicao"]=='2024-06-01']
print("\nProduto com data reposiçao = 2024-06-01: ")
print(preco_superior['Data_Ultima_Reposicao'])



"""
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
"""

