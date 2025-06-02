arquivo = None
try:
    arquivo =open("dados.txt")
    conteudo = arquivo.read()
    print("arquivo lido com suscesso")
except FileExistsError:
    print("erro arquiv nao encontrado")
except Exception as e:
    print(f" errp ap çer p ariqovp {e}")
else:
    print("processamento do arquivo concluciso com sucesso")
finally:
    if arquivo:
        arquivo.close()
        print("com sucesso")
"""
#Copiar o código
try:
    num_str = input("digite um numro: ")
    num_int =int(num_str)
    resultado = 10 /num_int
    #print("Erro: vc digitou letras")

except ValueError:
    print("errp emtrada omvaçodada valor incorreto")
except ZeroDivisionError:
     print("errp emtrada omvaçodada não divide por zero")
except Exception as e:
    print(f"pcprrrei i, errp {e}")

except ZeroDivisionError:
    print("Erro: Divisão por zero.")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Finalizando o bloco try-except.")

try:
    numero = int(input("Digite um numero "))
except ValueError:
    print("erro, digitou letra")



    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que será executado se a exceção ocorrer
    print("Erro: Divisão por zero não é permitida.")

Exemplos Práticos

Tratando uma exceção específica:

Copiar o código
try:
    numero = int(input("Digite um número: "))
    print(f"O número digitado foi {numero}.")
except ValueError:
    print("Erro: Você deve digitar um número válido.")


Tratando múltiplas exceções:

Copiar o código
try:
    arquivo = open("arquivo_inexistente.txt", "r")
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
except PermissionError:
    print("Erro: Permissão negada para acessar o arquivo.")


Usando else e finally:

O bloco else é executado se nenhuma exceção ocorrer.
O bloco finally é sempre executado, independentemente de ocorrer uma exceção ou não.
Copiar o código
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Erro: Divisão por zero.")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Finalizando o bloco try-except.")


Esses blocos tornam seu código mais robusto e ajudam a lidar com situações inesperadas de maneira elegante.
"""