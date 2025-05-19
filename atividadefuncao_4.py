#introdução fução
#funçao com print dentro dela para exibir o resultado da execução
#def soma():
#    print(+5)

#funçao com retorno (o eturn nao imprime nada e so retorno da execução
#def soma2():
#escrevauma funçao camada sete_irmaos. quando a funçao for chamada , ela dee imprimir os nomes dos sete irmãos em alfabetica.

#atividade 4
#escreva uma funçao chamada mesaXadrez,  que imprima um tabuleiro de xadrez feito de uns e zeros. 
#A funçao recebe um argumento inteiro, que especifica o comprimento do lado do tabelueiro. veja os exemplos abaixo para detalhes:


#numero = int(input("Quantas vezes: "))
def mesaXadrez(tamanho):
    linha = 0
    print(linha)
    while linha < tamanho:
        coluna = 0
        linha_texto =""
        while coluna < tamanho:
             if (linha + coluna) % 2 == 0:
                linha_texto += "1"
                #print("1" * tamanho)
             else:
                linha_texto +="0"
             coluna += 1
        print(linha_texto) 
        linha +=1     
print (mesaXadrez(10))




