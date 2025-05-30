
"""
##dicionarios
#usado para armazenar dados no formato: chave:valor
#são ordenados
#mataveis
#não permite elementos duplicados
#
#meu_dicionario ={}
#meu_dicionario["apina"] = "macado"
#meu_dicionario["nome"] = "jhon"

#print(meu_dicionario)
#print(meu_dicionario["nome"])

#palavra = input("Digite uma palavara: ")
#if palavra in meu_dicionario:
#    print("Traduçao:", meu_dicionario[palavra])
#else:
#    print("Palavras não encontrada")

#resultado = {}
#resultado["maria"]=5
#resultado["Julia"]=10
#soma=resultado["maria"] + resultado["Julia"]

#imprime chave valor
#dicionario={}
#dicionario["apina"]="Macado"
#dicionario["banana"]="Amarela"
#dicionario["cembalo"]="Cravo"
#for chave in dicionario:
#    print("Chave",chave)
#    print("Valor",dicionario[chave])

#popular
#lista para dicionário
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
#Pratica Dicionario:
#escreva uma funçao chamada histogram que recebe uma string como argumento.
#A funçao deve imprimir um histograma representando o numero de vezes que 
#cada letra ocorre na string. Cada ocorrencia de uma letra deve ser 
#representada por um asterisco na linha especifica para aquela letra.
#Por exemplo, a chamada ade funçao historgram("abba") deve imprimir

string=["usado para armazenar dados no formato chave:valor"]
def histogram(minha_string):
    histograma={}
    for letra in minha_string:
        if letra not in [histograma]:
            histograma[letra] = "i"
        histograma[letra] +=1
    return histogram
print(histogram(string))