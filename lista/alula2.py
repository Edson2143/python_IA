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
#a lista e impressa no começo e depois
"""
lista_pratica = [1,2,3,4,5,6]
print(lista_pratica)
opcao=int(input("informe 1 para remover ou 2 para adicionar: "))
#while True:
if opcao == 1:
    lista_del = lista_pratica.pop(3)
    print(lista_del)
    print(lista_pratica)
else:
    if opcao == 2:
        lista_pratica.insert(2,20)
        print(lista_pratica)
    else:
        print("opção errada")

lista=[]
print(lista)
while True:
    opcao = input("O que voce quer fazer ? + ou : ")
    if opcao =="+":
        if len(lista) ==0:
            lista.append(1)
        else:
            lista.append(lista[-1] + 1)
    else:
        if len(lista) == 0:
            print("A lista esta vazia")
        else:
            lista.pop(len(lista) - 1)
    print(lista)

#sort - Classificadção
lista =[0,45,68,98,78,98,65,23,35,54,47,89]
lista.sort()
#faz copia da lista original
lista_v2 = sorted(lista)
print(lista)
print(lista_v2)

#Lista: pratica
#Escreva um programa que peça ao usuario para digitar valores e os adicione a uma lista. 
#apos cada adições. a lista e impressa de duas maneiras diferenes:
# na ordem em que os itens foram adicionados
#ordenado do menor para o maior
#O programa sai quando usuario digita 0

lista_sorte=[]
while True:
    teste = input("Digite um valor: ")
    if teste != "":
        lista_sorte.append(teste)
        print("Lista (ordem de inserçao): ",lista_sorte)
        print("Lista (ordenada): ", sorted(lista_sorte))
    else:
        print("invalido")
        break

#Maximo , minimo a soma
lista_numeros = [0,45,78,6,32,15,7] #lista como argumento
print(max(lista_numeros))
print(min(lista_numeros))
print(sum(lista_numeros))

lista_mediana = [15,48,79,36,56,89,74,15,32]
def mediana(minha_lista: list): #pega numero do meio desde que seja lista
    ordenada = sorted(minha_lista)
    centro_lista =  len(ordenada)//2
    return ordenada[centro_lista]
print("Lista (ordenada): ", sorted(lista_mediana))
print(f"A mediana é {mediana(lista_mediana)}")
"""
#escreva uma funçao chamada temanho que receba uma lista como argumento e retorne
#o comprimeto da lista
def tamanholista_tamanho[12,10,11,13,40]
print len(lista_tamanho)