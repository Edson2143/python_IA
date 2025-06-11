
import pandas as pd
#atividade
#1 crie uma nova coluna chamada 'Rating_Metascore_Diff'que seja a diferença absoluta 
#entre 'Rating e (Matascore')/ 10),(Divida Metascore por 10 para coloca-lo numa escala 
#similar ao Rating).
#2 Mostre as  colunas 'Title','Rating','Metascore', e a nova 'Rating_Metascore_Diff 
# para os primeiros 5 filmes.
#3 Remova a coluna 'Description' do df_filmes Crie um novo DataFrame para isso, não 
# altere o original.
#4 Renomeie a coluna 'Votes' para 'Numero_Votos'. Faça isso no DataFrame original 
# usando inplace=True. Verifique se a coluna foi renomeada.

#O argumento inplace=True e usado em metodos do pandas(como.drop(),.sort_values(),.etc. 
#para indicar que a alteração deve ser feita diretamente no DataFrame original, 
#sem precisar reatribuir o resultado a uma variavael
#Base de dados
#pd. ler 
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
#1 crie uma nova coluna chamada 'Rating_Metascore_Diff'que seja a diferença absoluta 
#entre 'Rating e (Matascore')/ 10),(Divida Metascore por 10 para coloca-lo numa escala 
df_filmes['Rating_Metascore_Diff'] = df_filmes['IMDB_Rating']-(df_filmes['Meta_score'] / 10)
print("\n o dataframe agora tem uma nova coluna:")
print(df_filmes.head())

#2 Mostre as  colunas 'Title','Rating','Metascore', e a nova 'Rating_Metascore_Diff 
# para os primeiros 5 filmes.
df_filmes_sem_overview = df_filmes.drop(columns=['Overview'])
print("\nColuns apos remoçao da descrição:")
print(df_filmes_sem_overview.columns.tolist())

#3 Remova a coluna 'Description' do df_filmes Crie um novo DataFrame para isso, não 
# altere o original.
df_filmes.rename(columns={'No_of_votes': 'Numero_Votos'}, inplace=True)
#4 Renomeie a coluna 'Votes' para 'Numero_Votos'. Faça isso no DataFrame original 
# usando inplace=True. Verifique se a coluna foi renomeada.
print("\nVerificarçao das colunas apos raenomear 'No_of_votos':")
print(df_filmes.columns.tolist())

"""
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
df_filmes['Released_Year'] = pd.to_numeric(df_filmes['Released_Year'],
errors='coerce')
filmes_pos_2016 = df_filmes[df_filmes['Released_Year']>=2016]
[['Series_Title','Released_Year']]
#df_filmes['Released_Year'] = pd.to_numeric
#Primeiro_filme= df_filmes.iloc[[0,3],[3,9]]
print("\n primeiro filme  (linha coimpleta 2016:")
print(filmes_pos_2016)

#nova coluna:
df_filmes['Rating_x_10'] = df_filmes['IMDB_Rating'] * 10
print("\n o dataframe agora tem uma nova coluna:")
print(df_filmes.head())

#Conversao da coluna gross para float e ignorando erros caso fathar
df_filmes['Gross']=pd.to_numeric(df_filmes['Gross'],errors='coerce')
print(type(df_filmes['Released_Year']))

#Agora convertido o numero Gross em numero , e mais seguro fazer a comparação
df_filmes['Alta_receita'] = df_filmes['Gross']>1000
print("\n Dataframe com nova coluna 'Alta Receita (primieiras linhas) ")
print(df_filmes.head())
#Drop
#metodo drop remove uma linha (registro)ou coluna
df_filmes = df_filmes.drop('Poster_Link',axis=1)
print(df_filmes.head())
#axis = 0 excço p refotsrp
df_filmes = df_filmes.drop(4,axis=0)
print(df_filmes.head())

#10-06
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