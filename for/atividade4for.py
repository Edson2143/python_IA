#atividade 4
#escreva uma funçao chamada numeros_pares, que recebe uma lista de inteiros
# omo argumento. A funcao retorna uma nova lista contendo os numeros pares 
# da lista original.
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def numeros_pares(lista):
    impares=[]
    for numero in lista: 
        if numero % 2 != 0:
            impares.append(numero)
        #return (impares)
    return(impares)
print(numeros_pares(lista_original))
   #return [numero for numero in lista if numero % 2 == 0]
"""
#do professor 
l = [0,5,3,6,8,7,94,6,5,10,12,20]
def numeros_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares
print(numeros_pares(l))
"""


# Exemplo de uso:
#def lista_soma(lista1, lista2):
#   return [x + y for x, y in zip(lista1, lista2)]
#lista1 = [1, 2, 3]
#lista2 = [4, 5, 6]
#resultado = lista_soma(lista1, lista2)
#print(resultado)  # Saída: [5, 7, 9]