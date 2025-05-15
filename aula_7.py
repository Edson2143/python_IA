#re expreçoes regulares
#atividade 50
#crue um programa que solicite ao usuario para digitar uma serie de numeros ate que a soma desses numeros seja maior que 100
#mostre a soma total ao final
#s_n = int(input("Digite serie de numeros = "))
soma = 0
while  soma < 100:
    s_n = int(input("Digite serie de numeros = "))
    soma += s_n
    print(soma)
print(soma)






import re
import random
print(re.search("[A-Z]","Senha"))
print(re.search("[A-Z]","SeNha"))
print(re.search("[A-Z]","SeNha"))
print(re.search("[A-Z]","SeN1ha"))


numero_secreto = random.randint(1,200)
print(numero_secreto)