
import pandas as pd
#atividade 2 selecionando e filtrando filmes
#1.selecione apenas as colunas 'Title','Director", e "Year" do df_filmes. 
#  Mostre as primeiras 5 linhas.
#2.usando .iloc, selecione os filmes nas posições(linhas)10 a 15 e as colunas
#  nas posições 0a3
#3.definaa coluna 'Rank' como o indice do df_filmes Em seguida,use  .iloc 
#   para selecionar os filmes com Rank de 1 a 2 e mostrar apenas as colunas 
#  'Title' e 'Revenue(Millions)' Lembre-se de resetar o incidde depois ou 
#  usar uma copia do DataFrame para não alterar o original para as proximas 
#  atividade; df_temp = df_filmaes.set_index('Rank'))
#4.Filtre o df_filmes para mostrar apenas os filmes lançados(coluna 'Year')
#  a partir de 2016. Mostre 'Title' e 'Year'.

url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
#print(f"dados caregado : {url_filmes}")
#print(f"dados caregado : {df_filmes}")
#print("primeiroas 7 linhas do datFrame filmes head: ")
#print(df_filmes.head(7))
#print(df_filmes)
#selecionando linhas e e colunas especificar
selecao_especifica = df_filmes.iloc[[0,3],[1,2,9,3]]
print("primeiroas 5 linhas do datFrame filmes head: ")
print(selecao_especifica)
#exercico 2
Primeiro_filme= df_filmes.iloc[10:16,0:4]
print("\n primeiro filme  (linha coimpleta:")
print(Primeiro_filme)

#exercicio 3
df_temp=df_filmes.set_index('IMDB_Rating')
#top_5_rank = df_temp.loc[1:5,["Series_Title',Gross"]]
print("\n3.filmes de rank 1 a 5 com receita: ")
print(df_temp[['Series_Title','Gross']].head())
#print(top_5_rank)

#exercico 4
df_filmes['Released_Year'] = pd.to_numeric
Primeiro_filme= df_filmes.iloc[[0,3],[3,9]]
print("\n primeiro filme  (linha coimpleta:")
print(Primeiro_filme)

filmes_pos_2016 =df_filmes[df_filmes['Released_Year']>="2016"]




"""
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