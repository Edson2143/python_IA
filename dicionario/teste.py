#lista
def histogram(texto: str):
    contagem ={}
    for letra in texto:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1
    for letra in contagem:
        print(letra + ": " + "+" * contagem {letra})

histogram("abbacccc")
