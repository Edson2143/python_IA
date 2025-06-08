try:
    num_str = input("Digite um numero: ")
    num_int = int(num_str)
    resultado = 10 / num_int
    print(f"10 dIVIDIDO POR {num_int} é {resultado}")
    
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número") 
    
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero")
    
except Exception as e:
    print(f"Ocorreu um erro inesperado {e}")

#Esle só vai ser executado se não houve nenhum exceção.
else:
    print("Deu tudo certo")

#Executa mesmo que tenha erro ou não no try  
finally:
    if num_int == 0:
        num_int = int(input("Digite um numero: "))


    