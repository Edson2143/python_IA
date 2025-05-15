#atividade 15 operadoresde atribuiçao
#Usados para atribuir valores a variaveis. o mais basico e = mas existem formas abreviadas
# que combinam uma operação aritmetica com a abribuição.

#valor = 10 #valor da varialvel
#valor += 5 #variavel soma a 5 e o resultado e reatribuido a varialvel
#print(valor)
#valor *= 3 #a variavel valor e multiplicada por 3 e o resiltado e atribuidoa variavel
#print(valor)

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