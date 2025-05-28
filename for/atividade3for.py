
#atividade 3
#escreva uma funcao chamada Soma_Positivos, que recebe uma lista de inteiros 
#como argumento. A função retorna a soma dos valores positivos na lista.

def soma_positivos(lista):
    #testa para fazer tirar os numeros negativos e somar
    return sum(numero for numero in lista if numero < 0)

# Exemplo de uso:
numeros = [-5, 3, -1, 7, 2, -2, 8]
resultado = soma_positivos(numeros)
print(f"A soma dos números positivos é: {resultado}")
