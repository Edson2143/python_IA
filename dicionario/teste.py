lista_palavras = [
  "banana", "leite", "cerveja", "queijo", "leite azedo", "suco", "linguiça",
  "tomate", "pepino", "manteiga", "margarina", "queijo", "linguiça",
  "cerveja", "leite azedo", "leite azedo", "manteiga", "cerveja", "chocolate"
]
def contagens(minha_lista):
    palavras={}
    for palavra in minha_lista:
        if palavra not in palavras:
            palavras[palavra] = 0
        palavras[palavra] += 1
    return palavras
print(contagens(lista_palavras))
"""
dicionario={}
dicionario["apina"]="Macaco"
dicionario["banana"]="Amarela"
dicionario["cembalo"]="Cravo"
for chave in dicionario:
    print("Chave",chave)
    print("Valor",dicionario[chave])

minha_matriz=[[1,2,3],
             [3,2,1],
             [4,5,6]]
print(minha_matriz[0][1])
minha_matriz[1][0]=10
print(minha_matriz)


minha_lista=[7,2,2,5,2]
print(minha_lista[0])
print(minha_lista[1])
print(minha_lista[3])
print("A somo dos dois",minha_lista[0]+minha_lista[1])

numeros=[1,2,3,4,5,6]
numeros.insert(0,10)
print(numeros)
numeros.insert(5,50)
print(numeros)

numeros = []
numeros.append(5)
numeros.append(10)
numeros.append(3)
print(numeros)
#fatiar
letras = ["a","b","c","d","e","f"]
print(letras[1:4])
print(letras[:3])
print(letras[3:])
print(letras[::2])
print(letras[::-1])

minhalista = [10,20,30,40]
listalist = list(("jhon","pedro","Margarida"))
print(minhalista)
print(listalist)

def quadrado(x):
    print(f"Essa e minha propria função{x} e {x+x}")

quadrado(2)
quadrado(5)
quadrado(6)
quadrado(100)
"""