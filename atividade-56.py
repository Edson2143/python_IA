#atividade56
#escreva um programa que peça string ao usuario usando um loop. o pogrma imprime cada string sublinhada, como mostrado nos exemplos abiaxo. 
#a execução termina quando o usuario insere uma string vazia ou seja, apenas pressiona enter no prompt
estring = input("digite string = ")
while True:
    if estring == '':
        break
    else:
        print (f"\033[4m{estring}\033[0m")
        estring = input("digite string = ")

while True:
    texto = input("digite: ")
    if texto != "":
        print(texto)
        print("-"*len(texto))
    else:
        break

