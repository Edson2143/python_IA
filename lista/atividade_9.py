#atividade 9
#lista crescente
#peça ao usuario para digitar numeros ate que a lista esteja em ordem decrescente 
#(isto e oultimo numero for menor que o anterior), ao final, imprima todos os numeros
#difitados em ordem crescente.
def lista_Crescente():
    numeros=[]
    while True:
        numero=int(input("digite um numero: "))
        numeros.append(numero)
        if len(numeros) >1 and numeros[-1] < numeros[-2]:
            break
    numeros_ordenados = sorted(numeros)
    print("numeros digitados (ordem crescente):",numeros_ordenados)
lista_Crescente()
