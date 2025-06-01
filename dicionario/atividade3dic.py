#Atividade 3
#escreva uma funçao chamada invert(dicionario: dict), que recebe um dicionairo
#como argumento. O dicionario deve ser invertido no lugar para que valores se
#tornem chaves e CHAVES SE TORNEM VALORES
dict_original = {'a': 1, 'b': 2, 'c': 3}

# Invertendo o dicionário
dict_invertido = {valor: chave for chave, valor in dict_original.items()}

print(dict_invertido)
# Saída: {1: 'a', 2: 'b', 3: 'c'}


 Lista: Fatiamento (Slicing):
Permite extrair uma sub-lista (uma fatia) especificando [start:stop:step]. Semelhante ao range(), start é inclusivo, stop é 
exclusivo. step é opcional.