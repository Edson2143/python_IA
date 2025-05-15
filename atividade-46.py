# aula dia 13-05-2025
#atividade 46
#escreva um programa que peça um numer ao usuario. 
#o programa entao imprime todos os numeros inteiros maiores que zero, mas menores que a entrada
numero_auxiliar = 40
numero46 = int(input("digite um numero = "))
while numero46 >0:
    if numero46 > numero_auxiliar:
        print (numero46)
        numero46 += 1
    else:
        if numero46 < numero_auxiliar:
            print(numero46)
            numero46 += 1
        else:
            break


