#atividad 3
#crie uma lista com 5 frutas peça ao usuario um indice para exibir a fruta 
# correspondente. User Try e except para capturar indices invalidos e 
# exibir " indice fora do alcance"


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
