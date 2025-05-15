#atividade 48
#altere o programa do exercicio anteior par que o usuairo posssoa inserir 
#tambem a base que e multiplicada (no programa aneriror , a base era sempre 2)

#escreva um programa que peça um ao usuario para digitar um limite superuior.
# o programa então imprime numeros de modo quecada numeros subsegquente seja o anerior dobrado,
# começando do numero 1. ou seja o programa imprime potencias de dois em ordem. 
#A execuçao do programa termina quando o proximo numero a ser impresso for maior que
#o limite definido pelo usuairo. nenhuma numero maior que o limite deve se impresso

numero_superior = int(input("Digite numero usuario = "))
numero_anterior = int(input("Digite numero anterior = "))

numero = 1
while numero_anterior <= numero_superior:
    print(numero_anterior)
    numero_anterior *= numero_superior
    print (numero_anterior)



base= int input 