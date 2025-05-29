"""
minha_string = "Quantas madeiras um esquilo poderia emplilhar " \
               "se um esquilo pudesse empilhar modeiras"
print(minha_string.count("a"))

minha_lista = [1,2,3,5,6,6,9,9,8]
print(minha_lista.count(6))

#replace
minha_palavra = "oi,oi,oi, amigos, Ola"
nova_palavra = minha_palavra.replace("Oi","" "Olá")
print(nova_palavra)

lista_bidimencional = [
    [0,1,2,3],
    [0,8,6,9],
    [1,2,7,4],
    [4,5,6,8]
]
print(lista_bidimencional[3][3])

#lista pratica:
#escreva umafunçaochamada conta_elementos_match(minha_matriz: list, elemnto: 
#int), que recebe um array bidimensional de inteiros e um unico valor inteiro
#como seus argumentos. a função entao conta quantos elementos dentro da 
#matriz correspondem ao valordo argumento

listaBi=[
    [1,2,3,4,5,6],
    [10,11,12,13,14,15],
    [20,23,25,26,24,25],
    [40,41,42,43,44,50]
]

def conta_elementos_match(minha_matriz, elemento):
    contagem = 0
    for linha in minha_matriz:
        for item in linha:
            if item==elemento:
                contagem+=1
    return contagem

print(conta_elementos_match(listaBi),[4])
"""
#escreva um algoritimo que imprime na ela o tabuleiro de sudoku baseado na lista enviada no teams
sudoku=[[9, 0, 0, 0, 8, 0, 3, 0, 0],
  [0, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [0, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]

#def conta_elementos_sudoku(minha_sud,elemento):
for linha in sudoku:
    for item in linha:
        if item==0:
            print("_",end="")
        else:
            print(item,"",end="")

    print("")