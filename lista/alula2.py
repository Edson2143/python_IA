"""
#fatiar
letras = ["a","b","c","d","e","f"]
print(letras[1:4]) # ele corta de 1 ao elmento de incide 4
print(letras[:3]) #corta do inicio ate o 3-1
print(letras[3:]) #do indice 3 ate ofinal     
print(letras[::2]) #todos, com passo 2
print(letras[::-1]) # lista invertidas

#adicionar itens a lista

numeros =[]
numeros.append(5)
numeros.append("edson")
print(numeros)

#paratica 3

lista = []
inicio = 0
quantidade = int(input("quantos numero "))
while quantidade > inicio:
    numero = int(input(f"insira um numero {inicio + 1}"))
    lista.append(numero)
    print(lista)
    inicio += 1
    print[lista]
"""
#pratica 4
numeros=[10,50,36,25,14]
print(numeros)
#numeros.append(5)
#numeros.append(3)
#numeros.append(10)
#acicionar itens em  lugar  especificos
numeros.insert(1,50)
numeros.insert(0,20)
numeros.insert(7,200)
print(numeros)

#remover itens pelo indice
numeros.pop(0)
numero_deletado=numeros.pop(0)
print(numero_deletado)
print(numeros)


lista_nova = [10,20,10,30,50,60,70]
#remove criar exemplo

#pratica 5
#escrever um programa que peça ao usuario para escolher entre adiçao e reomação.
# dependendo da escolha, o programa adiciona um item ou remove um item do final 
# de uma lista. o item que e adicionado deve ser sempre uma amais que o utilmoitem 
# da lisa. o primeiro item a ser adicionadodeve ser 1

lista_pratica =[10,11,12,13,14,15]
opcao=input("informe 1 para remover ou 2 para adicionar")
while True:
    if opcao == 1:
        lista_pratica  