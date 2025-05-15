#atividade51
#len,  re,  random funçao expreçoes regulares
#escreva um programa que continue solicitando ao usuario para digitar 
# uma senha ate que ele inseira uma senha que tenha  pelo menos 8 caracteres,
# contenha pelo menos uma letra maiúscula, uma letra mnínuscula e um numero 
#len funçao expreçoes regulares
import re
import random

while True:
    nome_usuario = input("informe o nome = ")
    temMaiuscala = re.search("[A-Z]",nome_usuario)
    temMinuscula = re.search("[A-Z]",nome_usuario)
    temNumero = re.search("[0-9]", nome_usuario)
    if len(nome_usuario) < 8:
        print("senha precisa ter 8 cararc")
    elif temMaiuscala == None:
        print ("tem que ter maiuscula")
    elif temMinuscula == None:
        print ("tem que ter minuscula")
    elif temNumero == None:
        print("tem que ternumero")
    else: 
        print ("senha compativel")
        break

import re
print (re.search("[A-Z]")


