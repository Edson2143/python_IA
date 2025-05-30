#Atividade 3
#escreva uma funçao chamada invert(dicionario: dict), que recebe um dicionairo
#como argumento. O dicionario deve ser invertido no lugar para que valores se
#tornem chaves e CHAVES SE TORNEM VALORES

#def dicionario():


from collections import defaultdict
def collect_dictionary(obj):
  inv_obj = defaultdict(list)
  for key, value in obj.items():
    inv_obj[value].append(key)
  return dict(inv_obj)
print(collect_dictionary)

