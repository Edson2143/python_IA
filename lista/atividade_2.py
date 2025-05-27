#atividade 2
#escreva uma funçao chamada range, que recebe uma ista de inteiros como argumento. 
#A funçao retorna a diferença entre o menor e o maior valor na lista

lista_inteiro = [10,20,12,30,42,20]
lista_argumento = [1,3,4,6,7]
print(max(lista_inteiro)-(min(lista_argumento)))

valores = [8,3,15,1,9]
def diferenca_extremos(lista):
    return max(lista) - min(lista)
print(diferenca_extremos(valores))

"""
lista = [10,25,36,65,45,98,78]
def media(lista):
    return sum(lista) / len(lista)
print(media(lista))



#Maximo , minimo a soma
lista_numeros = [0,45,78,6,32,15,7] #lista como argumento
print(max(lista_numeros))
print(min(lista_numeros))
print(sum(lista_numeros))
"""