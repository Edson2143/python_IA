#atividade52
#Crie um programa que peça ao usuario para adivinhar um numero entre 1 e 100. O programa deve continuar 
#pedindo ate que o usuario adivinhe o numero corretamene. de dicas se o numero e maior ou menor a da tentavia
import random
numero_informado = random.randint(1,100)
numerodevezes = 0
while True:
    tentativa = int(input("Digite um numero (entre 1 e 100)= "))
    numerodevezes += 1
    if n1 > 1 and n1 < 100:
        if n1 == numero_informado:
            print ("numero correto")
            break
        else:
            if n1 > numero_informado:
                print("numero maior que informado")
            else:
                print("numero menor que informado")
