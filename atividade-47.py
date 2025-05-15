#atividade 47
#escreva um programa que peça um ao usuario para digitar um limite superuior.
# o programa então imprime numeros de modo quecada numeros subsegquente seja o anerior dobrado,
# começando do numero 1. ou seja o programa imprime potencias de dois em ordem. 
#A execuçao do programa termina quando o proximo numero a ser impresso for maior que
#o limite definido pelo usuairo. nenhuma numero maior que o limite deve se impresso

numero_superior = int(input("Digite numero usuario = "))
numero_anterior = 1
#numero_resultado = 0
while numero_anterior <= numero_superior:
    print(numero_anterior)
    numero_anterior *= 2
    print (numero_anterior)




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


