#atividad 2 
#peca ao usuario dois numeros para diicir . use try e except para capturar 
#erro de divisao por zero e exibir uma mensagem apropriada.ModuleNotFoundError

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
