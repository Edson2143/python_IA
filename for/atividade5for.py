#atividade 5
#escreva uma funçao chamada lista_soma que recebe duas listas de inteiros 
#como argumentos. a Funçao retorna uma nova lista que contem as somas dos 
#itens em cada indice nas duas listas originais. voce pode assumir que ambas
#as listas taem o mesmo numero de itens

def lista_soma(lista_original0, lista_original1):
    return [x + y for x, y in zip(lista_original0, lista_original1)]
lista_original0=[1,2,3,5,6,7,8,9,90]
lista_original1=[3,7,9,11,13,15,17,19,3]
resultado = lista_soma(lista_original0, lista_original1)
print(resultado)
#lista1 = [1, 2, 3]
#lista2 = ['a', 'b', 'c']



#zipped = zip(lista1, lista2)

# Exemplo de uso:
resultado[]
def lista_soma(listax, listay):
    for i in range(listax,listay)
        soma= lista1[i] + lista[i]
#   return [x + y for x, y in zip(lista1, lista2)]
#lista1 = [1, 2, 3]
#lista2 = [4, 5, 6]
#resultado = lista_soma(lista1, lista2)
#print(resultado)  # Saída: [5, 7, 9]