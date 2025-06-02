#digite um nuero inteiro use Try e except para grantir que se o usuario 
#digitar algo que nao seja numero, o programa não quebre e mostre uma
# mensagem de erro personalizado

try:
    numero = int(input("digirte o numero "))
except ValueError:
    print("numero não é inteiro")
else:
    print(f"Resultado: {numero}")
finally:
    if numero %2:
        print ("numero nao e inteiro digite novamente")
        numero = int(input("digirte o numero "))
    else:
        print("Finalizando o bloco try-except.")
