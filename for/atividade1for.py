#atividade 3
#escreva uma funcao chamada Soma_Positivos, que recebe uma lista de inteiros 
#como argumento. A função retorna a soma dos valores positivos na lista.

def soma_positivos(lista):
    #testa para fazer tirar os numeros negativos e somar
    return sum(numero for numero in lista if numero > 0)

# Exemplo de uso:
numeros = [-5, 3, -1, 7, 2, -2, 8]
resultado = soma_positivos(numeros)
print(f"A soma dos números positivos é: {resultado}")

"""
#atividades 2
#Escrevauma funçao chamada anagramas, que recebe duas strings como argumentos.
#a funçao retorna True se as string são anagrams uma das outra. Duas palavras 
#são anagrams se elas contem exateamente os mensos caracteres. Dica:
#a funçao sorted tambem pode ser usada em strings.

def  anagrama(anagramas1, anagramas2):
    return sorted(anagramas1)==sorted(anagramas2)

print(anagrama("amor", "roma")) # Verdadeiro
print(anagrama("tabby", "batty")) # Verdadeiro


#atividade 1
#escreva uma funçao chamada lista_estrelas, que recebe uma lista de inteiros como 
# argumento. a funçao deve imprimir linhas de caracteres de asteisco. os  numeros 
# na lista especificam quantos asteriscos cada linha deve ConnectionError
#Por exemplo com a chamada de funçao lista_estrelas([3,7,1,1,2]) o seguinte deve ser 
#impresso:
#**
#*******
#*
#*
#**
lista_estrelas =[3,7,11,2]
def estrelasCaracter(lista: list):
    for i in lista:
        estrelas = "*" * i
        print(estrelas)
estrelasCaracter(lista_estrelas)


#criando uma lista a partir do range
numero =(range(3, 15))
#print(numero, [5])
for i in numero:
    print(i)

#Pratica for e range
#escrevea um programa que peça ao usuario um inteiro positivo N. 
#o programa entao imprime tdos os numeros entre -N e N inclusive,
#mas deixa de forao numero O Cada numero  deve ser impresso em uma linha separada.
N= int(input("Digite = "))
for i in range(-N, N+1):
    if i != 0:
        print(i, end="")


inteiro = int(input("digite um numero = "))
for inteiro in range(inteiro):
    if range(inteiro) != 0:
        print (inteiro +1)
#        print (inteiro +1, end=", ")

#Pratica
# escreva um programa que peça ao usuario para digitar uma string. 
# O programa então imprime  cada caractere de entrada em uma lista 
# separada. Depois de cada caractere deve haver um asterisco(*) 
# impressso em sua propria linha.

#range no for
#aqui 2 argumento sao quantas iterações quero que o codigo execute
for I in range(5,20):
    print(I)    
#repete o bloco de codigo pulando de 2 em 2
for J in range(0,10,2):
    print(J)    

lista = input("Difite nome = ")
for caractere in lista:
    print(caractere, end="*")
#    print(caractere, "*")




lista= ["Marta","madalena","pedro","alex","1"]
for nome in lista:
    if len(nome) > 2:
        print(nome)
    else:
        print(f"O{nome}, tem nmesmo caracteres 3")
"""