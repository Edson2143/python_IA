
import pandas as pd
#selicionando uma coluna
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)

titulos_filmes = df_filmes['Series_Title']
print("primeiro 5 filmes")
print(titulos_filmes.head)

#selicionar multiplas colunas
filmes_selecionados = df_filmes[['Series_Title','Genre','IMDB_Rating']]
print (f"\nDataframe com titulo, Genero e Nota")
print(filmes_selecionados.head())

#elementos a primeira linha
#Iloc e usado para selecionar linhas por indice numericos
Primeiro_filme= df_filmes.iloc[0:3]
print("\n primeiro filme  (linha coimpleta:")
print(Primeiro_filme)

#selecionando linhas e e colunas especificar
selecao_especifica = df_filmes.iloc[[0,3],[1,4]]
print("\n Printando uma seleçao especifica, linha 0 e 3 e coluna 0 e 4")
print(selecao_especifica)

#selecionando dados com .loc
#Localiza os dados pelos rotulos.
df_filmes_idx = df_filmes.set_index("Series_Title")
print("\n Definimos o indice agora como series title")
print(df_filmes_idx.head())

#dados do filme onde o indice virou o nome do filme exeplo abaixo
Poderoso = df_filmes_idx.loc["The Godfather"]
print('\nDados do filme : the godfather')
print(Poderoso)
#Filtrar  os dados baseados em condicoes (Boolean indexing0)
df_filmes_bem_avaliados = df_filmes[df_filmes["IMDB_Rating"]<=8.5]
print("\nFilmes com nota >+ 8.5 (Primeira linha):")
print(df_filmes_bem_avaliados['Series_Title'].head())

#filtrar filmes de acao
filme_acao = df_filmes[df_filmes["Genre"].str.contains("Action",na=False)]
print("\n foç,es qie cpmte, p gemerp 'Ation'")
print(filme_acao[['Series_Title','Genre']].head())

"""
print("dados caregado")
   

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