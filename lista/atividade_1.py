#atividade 1
#escreva uma funcao chamada media que recebe uma lista de inteiros como argumento.
# A funcao retorna amedia aritimetica dos valores na lista.
#def mediana(minha_lista: list): #pega numero do meio desde que seja lista

lista = [10,25,36,65,45,98,78]
def media(lista):
    return sum(lista) / len(lista)
print(media(lista))



