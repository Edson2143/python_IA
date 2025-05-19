#introdução fução
#funçao com print dentro dela para exibir o resultado da execução
#def soma():
#    print(+5)

#funçao com retorno (o eturn nao imprime nada e so retorno da execução
#def soma2():
#escrevauma funçao camada sete_irmaos. quando a funçao for chamada , ela dee imprimir os nomes dos sete irmãos em alfabetica.

#atividade 5
#escreva uma funçao chamada quadradotring, que recebe um argumento de stringe um argumento inteiro e imprime um quadrado de caracteres conforme especificado pel oexemplo abaixo
#aybab
#tuayb
#Abtua
#ybatt
#uayba


#numero = int(input("Quantas vezes: "))
def quadradoString(argumento):
    linha = 0
    
    print(linha)
    while linha < argumento:
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
print (quadradoString("aybab","tuayb","Abtua","ybatt","uayba"))




