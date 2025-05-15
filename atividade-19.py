#atividade 19 estrutura condicional: IF: atividade
#escreva um programa onde voce  armazena 4 valores de variaveis (nome, ciadee, estado e cep),
#e peça para o usuuario escrever um nome no input. 
#se o nome for igual ao definido na variavel ele exeibira os dados das outras variavel. 
#se for diferente exiba a mensagem("esse usuario nao existe em nosssas bases de dados")
valores_fixo_1 = ("Edson")
valores_fixo_2 = ("curitiba")
valores_fixo_3 = ("Parana")
valores_fixo_4 = ("81220-140")
valores_1 = input("informe valor 1 = ")
#valores_2 = input("informe valor 2 = ")
#valores_3 = input("informe valor 3 = ")
#valores_4 = input("informe valor 4 = ")
if valores_1 == valores_fixo_1:
    print(f"{valores_fixo_1} {valores_fixo_2} {valores_fixo_3} {valores_fixo_4}")
else:
    print("esse usuario nao existe em nosssas bases de dados")

#*/*/*/*/*/*/*/*/*/*/*/*/**/*/*/*/*/*/*/*/*/
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