#introdução fução
#funçao com print dentro dela para exibir o resultado da execução
#def soma():
#    print(+5)

#funçao com retorno (o eturn nao imprime nada e so retorno da execução
#def soma2():
#escrevauma funçao camada sete_irmaos. quando a funçao for chamada , ela dee imprimir os nomes dos sete irmãos em alfabetica.

#atividade 3
#escreva umafunçao chamada quadrado_hasjtag(tamanho), que  recebe um argumento inteiro. 
#A funçao imprime um quadrado de caracteres hash, e o  argumento especifica o comprimento do lado do quadrado 

numero = int(input("Quantas vezes: "))
def quadrado_hashtag(tamanho):
    contador = 0
    while contador < tamanho:
        print("*" * tamanho)
        contador += 1
print (quadrado_hashtag(numero))
