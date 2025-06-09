
import pandas as pd
#crando uma  series
"""
idade= pd.Series([1,2,3,4,5,6])
print(idade)

idades_nomes = pd.Series([1,2,3,4],index=["ana","joão","Maria","carlos"])
print(idades_nomes)
"""
#data frame
dados_alunos ={
    "nome":["ana","joão","Maria","carlos"],
    "Idade" :[1,2,3,4],
    "Curso" :["engenharia","medicina","direito","professor"]
    }
df_alunos = pd.DataFrame(dados_alunos)
print(df_alunos)