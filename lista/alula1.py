"""
#criar uma lista 
#minha_lista = [10.30.15]
#aces
#print(minha_lista[0])
#print(minha_lista[1])
#print(minha_lista[2])

#trabahando com lista
#resultado = minha_lista[0] + minha_lista[2]


#lista:Pratica
#escreva um programa que inicialize uma lista com os valores [1,2.3.4.5], 
#Entao o programa deve pedir ao usuario um indice e um novo valor, substritutir 
#o valor no indice fornecido e imprimir a lista novamente. isso deve ser repetido ate
#que o usuario forneça -1 para o indici.
# corrigir            
# Inicializa a lista com valores
inicio_lista = [0,1, 2, 3, 4]
while True:
    # Exibe a lista atual
    print("\nLista atual:", inicio_lista)
    # Solicita ao usuário um índice
    novo_valor = input(("digite novo valor: "))
    if novo_valor == -1:
        print("ok deu certo")
        break
    if novo_valor <= 0 or novo_valor >= len(inicio_lista):
        novo_valorovo_valor = input(("digite novo valor : "))
        numeros[novo_valor] = novo_valor
        print("Índice inválido. Tente novamente.")
    else:
        print("digite novo valor 1: ")
    print("lista atual",numeros)
    

inicio_lista = [1,2,3,4,5]
while inicio_lista[0]:
    inicio_lista [0:1] = ("eric")
    print(inicio_lista)
    break    

# Inicializa a lista com valores
lista = [10, 20, 30, 40, 50]

while True:
    # Exibe a lista atual
    print("\nLista atual:", lista)
    
    # Solicita ao usuário um índice
    try:
        indice = int(input("Digite o índice que deseja substituir (ou -1 para sair): "))
        if indice == -1:
            print("Encerrando o programa. Até mais!")
            break
        if indice < 0 or indice >= len(lista):
            print("Índice inválido. Tente novamente.")
            continue
        
        # Solicita ao usuário o novo valor
        novo_valor = int(input("Digite o novo valor: "))
        
        # Substitui o valor no índice fornecido
        lista[indice] = novo_valor
    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros.")
"""

numeros = [1,2,3,4,5]
numeros[3] = 35
print (numeros)