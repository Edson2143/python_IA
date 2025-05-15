#atividade58
#escreva um programa que peça ao usuario string, entao imprima um quadro de *caracteres com a palavra no centro. 
#A largura do quadro deve ser de 30 caracteres. voce pode assumir quea string de entrada sempre cabera dentro do quado

#se o comprimento da sequencia de entrada for um numero impar, voce pode imprimir a palavra em qualquer um dos dois 
#possiveis locais centrais
estring = input("digite string 58 = ")
hash="*"
contador = 0
while True:
    if contador != 30:
        print(hash)
    else:
        print((hash),estring,(hash))
        contador = 0
        if contador != 30:
            print(hash)
        else:
            break






estring = input("digite string 57 = ")
#print(len(estring) == 20)

if len(estring) < 20:
     asteriscos = "*" * (20 - len(estring)) 
     resultado = asteriscos + estring
else:
    resultado = estring[:20]
print("resultado :", resultado)    
#:20 serve paea contar os caracteres 

estring = input("digite string = ")
print(len(estring) == 20)
if len(estring) != 20:
     estring = input("digite string = ")
else:
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

