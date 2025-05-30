#atividade 1
#escreva um aplicativo de lista telefonica. ele deve funionar da seguinte 
#forma:
#comando(1 busca, 2 adiciona, 3 sai): 2




print("1 busca ")
print("2 adiciona ")
print("3 sai ")
opcao = int(input("Digite opcao "))
def lista_tel(texto):
    telefonica={}
    if opcao == 1:
        nome=input("Digite o nome = ")
        for nome in texto:
            print(nome)
            telefonica[nome] +=1
    else:
        if opcao == 2:
            
    print(telefonica)    

lista_tel("joao")




"""
#lista
def histogram(texto: str):
    contagem ={}
    for letra in texto:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1
    for letra in contagem:
        print(letra + ": "+"+" * contagem {letra})

histogram("abbacccc")
"""