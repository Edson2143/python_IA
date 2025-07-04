#atividad 3
#crie uma lista com 5 frutas peça ao usuario um indice para exibir a fruta 
# correspondente. User Try e except para capturar indices invalidos e 
# exibir " indice fora do alcance"
"""
lista=["banana","laranja","abacate","uva"]
indice = 0

try:
    numero = int(input("digirte o numero "))
    if len(lista) not in lista and indice > len(lista):
        print ("não existe na lista")
    else:
        print (lista)
except ValueError:
    print("numero não é inteiro")
else:
    print(f"Resultado: {numero}")
finally:
    if numero %2:
        print ("numero nao e inteiro digite novamente")
        numero = int(input("digirte o numero "))
    else:
        print("Finalizando o bloco try-except.")
"""

# Lista de frutas
frutas = ["Maçã", "Banana", "Laranja", "Uva", "Manga"]

# Solicita ao usuário um índice
try:
    indice = int(input("Digite um índice (0 a 4) para exibir a fruta correspondente: "))
    print(f"A fruta correspondente ao índice {indice} é: {frutas[indice]}")
except IndexError:
    print("Índice fora do alcance! Por favor, insira um número entre 0 e 4.")
except ValueError:
    print("Entrada inválida! Por favor, insira um número inteiro.")
