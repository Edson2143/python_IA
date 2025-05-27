#atividade 3
#escreva uma funçao que peça ao usuário para digitar 5 nomes, se o nome ja estiver na
#lista, ele na deve ser adicionado novamente. ao final imprima todos os nomes cadastrados.
nomes = ["edson","eric","jorge","marcos","jorge"]
entrada=input("Entre com um nome ")
def estiver(nomes):
    return(nomes)

print(entrada in(nomes))

lista_nomes =[]
def nomes_unicos():
    while len(lista_nomes) < 5:
        nome = input("Quqal nome " )
        if nome in(lista_nomes):
            print("nome ja existe")
        else:
            lista_nomes.append(nome)
        return lista_nomes
print(nomes_unicos)


"""
lista_inteiro = [10,20,12,30,42,20]
lista_argumento = [1,3,4,6,7]
print(max(lista_inteiro)-(min(lista_argumento)))

valores = [8,3,15,1,9]
def diferenca_extremos(lista):
    return max(lista) - min(lista)
print(diferenca_extremos(valores))


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