""" #dicionário

#Usado para armazenar dados no formato: Chave:valor
#são ordenados
#mutáveis
#Não permite elementos duplicados

meu_dicionario = {}
meu_dicionario["apina"] = "macaco"
meu_dicionario["nome"] = "John"

# print(meu_dicionario)
# print(meu_dicionario["nome"])


    
    
resultado = {}
resultado["maria"] = 5
resultado["Julia"] = 10

soma = resultado["maria"] + resultado["Julia"]

#imprimir chave:valor

dicionario = {}

dicionario["apina"] = "Macaco"
dicionario["banana"] = "Amarela"
dicionario["cembalo"] = "Cravo"

for chave in dicionario:
    print("Chave:",chave)
    print("Valor", dicionario[chave])
    
#Popular """

lista_palavras = [
  "banana", "leite", "cerveja", "queijo", "leite azedo", "suco", "linguiça",
  "tomate", "pepino", "manteiga", "margarina", "queijo", "linguiça",
  "cerveja", "leite azedo", "leite azedo", "manteiga", "cerveja", "chocolate"
]

def contagens(minha_lista):
    palavras = {} # "chave":"valor"
    for palavra in minha_lista:
        if palavra not in palavras:
            palavras[palavra] = 0            
        palavras[palavra] += 1
    return palavras
    
print(contagens(lista_palavras))    
