#atividade57
#escreva um progrma que peça ao usuario uma string e entao a imprima de modo que exatamente 20 caracteres
#seja exibidos. se a entrada for menor que 20 caracteres, o começo da linha e preenchido com * caracteres.
estring = input("digite string = ")
#print(len(estring) == 20)

if len(estring) < 20:
     asteriscos = "*" * (20 - len(estring)) 
     resultado = asteriscos + estring
else:
    resultado = texto[:20]
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

