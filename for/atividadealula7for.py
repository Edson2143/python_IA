#ativadade 7
#O jogo da velha e jogado em uma grade 3 por 3 por dois jogadores que se 
#revezam inserindo cruzes e circulos. Se qualquer jogador conseguir colocar
#tres de seus proprios simbolos em qualquer linha, coluna ou diagonal, 
#ele ganha se nenhum jogador conseguir isso, é um empate. 
#Escreva uma funçao chamada:
#jogue_o_jogo(mesa:list, x: int, y: int,caracter:str), que coloca o simbolo 
#dado nas coordenadas dadas no tabuleiro Os valores das coordenadas
#no tabuleiro estão entre 0 e 2
#mes=
#def jogue_o_jogo(mesa: list, x: int, y: int, caracter: str):
#    mesa[x][y] = caracter

#x_m_l=input("digite linha  = ")
#y_m_c=input("digite coluna = ")
#c=input("digite caracter = ")
#contador=0
#print([x_m_l],[y_m_c],c)
#while True:
#    if contador >=9:
#        print([x_m_l][y_m_c],c)
#        contador +=1
#    else:
#        print("fim")


#jogo da velha
#mesa 3x3
mesa = [
    ["","",""],
    ["","",""],
    ["","",""]
    ]
#conta até 3x3 = 9
contador = 0
print(F"Tempo: {contador} - Olá jogador 1, comece o jogo com X. BOA SORTE!")
 
def jogue_o_jogo(mesa,linha,coluna,caracter):
    mesa[linha][coluna] = caracter
    exibe_resultado()
    #testa modulo para ver se é inteiro
    if contador % 2 != 0:
        jogador = "1 (x)"
    else:
        jogador = "2 (O)"

  
    print(f"Tempo {contador} - Ótimo jogada, agora é a vez do jogador {jogador}")
    print("")
 
def exibe_resultado():
    for linhas in mesa:
        for items in linhas:
            if items == "":
                print("_ ",end="")
            print(items,end=" ")
 
        print(" ")
#testa para while para ver para inserir informação linhs,coluna,caracter
#colocar validação    
while True:
    linha = int(input("Qual a linha: "))
    if linha == 0 or  1 or 2:
        coluna = int(input("Qual a coluna: "))
        caracter = input("Qual o caracter: ")
        jogue_o_jogo(mesa,linha, coluna, caracter)
    else:
        print("linha incorreta")
        break   
    contador += 1
    if contador == 9:
        exibe_resultado()
        break
 



#for linha in sudoku:
#    for item in linha:
#        if item==0:
#            print("_",end="")
#        else:
#            print(item,"",end="")#

#    print("")
