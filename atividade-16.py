#tividade 16 estrutura condicional: IF: atividade
#ecreva um programa que solicite ao usuairo um numero  inteiro. se o numero for menor que zero o programa devera imprimir
#o numero como está

number = int(input("entre com number = "))
if number > 0:
    number *= -1
    print(f"resultado, {number}")
else:
    print(number)


n1= 20
n2 = 20
n3 = 35
n4 = 40
print (n1>n2 and n2 < n3)

if n1 == n2 or n3 ==n4:
    print("verdadeiro")
else:
    print("falso")
    
numero = int(input("entre com um numero : "))
if numero  <0:
    print("essenumero e negativo")
if numero > 0:
    print("esse numero e positivo")
if numero == 0:
    print("o número é 0")

senha = input ("entre com senha = ")
if senha == ("hellokitty"):
    print("senha conrreta")
else:
    print("errou menu nobre")

inteiro = int(input("entre com numero "))
if inteiro == 1984:
    print("onwell")
else:
    print("errou", inteiro)