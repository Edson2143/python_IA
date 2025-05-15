#atividade 17 estrutura condicional: IF: atividade
#escreva um programa que solicite ao unuario um nmero interio. o programa deve entao imprimir a maguinitura do numero de acordo com os exemplos a seguir.
#exemplo de saida

#1. por favaro digite um numero :950
# este numero e menor que 1000 obrigado
#2. por foavor difite um numero :59
# este numero e menor que 1000 este numero  é menor que 100 obrigado
#3. por favor digite o numero: 2
# este numero e menor que 1000 este numero e menor que 100 este numero que 10 obrigado
#4. por favor digite um nuemro 1123
#   obrigado

numero_18 = int(input("dig numero 950 = "))
if numero_18 < 1000:
    print("este numero e menor que 1000 Obrigado")
    numero1_18 = int(input("dig numero 59 "))
    if numero1_18 < 59:
        print("este numero é menor 100, obrigado")
        numero2_18 = int(input("digite numero 2 "))
        if numero2_18 < 2:
            print("este numero menor que 10 obrigado")
        else:
            numero3_18 = int(input("Digigite numero 1123 = "))
            print(f"numero obrigado  {numero3_18}")            
    else:
        numero3_18 = int(input("Digigite numero 1123 = "))
        print(f"numero obrigado {numero3_18}")
else:
    numero3_18 = int(input("Digite numero 1123 = "))
    if numero3_18 == 1123:
        print(f"numero obrigado {numero3_18}")
    else:
        print ("numero fora do enunciado")


#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
usuario = input("informe o nome = ")
preco_unico = 5.90
if usuario != "Jerry":
    num_por = int(input("Numero porçao "))
    preco_total= (num_por*preco_unico)
    print(preco_total)
    #print (f"preço total, {num_por * preco_unico}")
else:
    print("nome incorreto")

number = int(input("entre com number = "))
if number > 0:
    number *= -1
    print(f"resultado, {number}")
else:
    print(number)

n1 = 20
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