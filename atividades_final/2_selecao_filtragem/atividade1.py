
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
print(data_reposto['Data_Ultima_Reposicao'])

#13. Quais produtos são fornecidos pela 'Fazenda Sol Nascente' E são da categoria 'Fruta'?
data_fornecido = (df_filmes['Fornecedor'] == 'Nunes') & (df_filmes['Categoria'] == 'Fruta')
produtos_filtrados = df_filmes[data_fornecido]
print("\nProduto Fornecido")
print(produtos_filtrados)

#14 Selecione os produtos que são 'Fruta' OU têm Estoque_Kg maior que 150 Kg.
data_frutas = (df_filmes['Categoria'] == 'Fruta') #& (df_filmes['Estoque_Kg'] >= 150)
produtos_selecionados = df_filmes[data_frutas]
print("\nFrutas >= 150 kg")
print(produtos_selecionados)
