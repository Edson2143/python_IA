#atividad 4
#peca ao usuario o nome de um arquivo para abrir. use try e exceptpara 
# lidar com o erro caso arquivo não exista, mostrando uma mensagem 
# "Arquivo não enontrado"

arquivo = None
try:
    arquivo =open("dados.txt")
    conteudo = arquivo.read()
    print("arquivo lido com suscesso")
except FileNotFoundError:
    print ("arquivo enexistente")
except FileExistsError:
    print("erro arquivo nao encontrado")
except Exception as e:
    print(f" erro ao abrir o arquivo {e}")
else:
    print("processamento do arquivo concluciso com sucesso")
finally:
    if arquivo:
        arquivo.close()
        print("com sucesso")


"""
lista=["banana","laranja","abacate","uva"]
indice = 0

try:
    numero = int(input("digirte o numero "))
    if len(lista) not in lista and indice > len(lista):
        print ("não existe na lista")
    else:
        print (lista)
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


# Lista de frutas
frutas = ["Maçã", "Banana", "Laranja", "Uva", "Manga"]

# Solicita ao usuário um índice
try:
    indice = int(input("Digite um índice (0 a 4) para exibir a fruta correspondente: "))
    print(f"A fruta correspondente ao índice {indice} é: {frutas[indice]}")
except IndexError:
    print("Índice fora do alcance! Por favor, insira um número entre 0 e 4.")
except ValueError:
    print("Entrada inválida! Por favor, insira um número inteiro.")
"""