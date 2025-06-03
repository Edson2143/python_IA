
#Arquivo :Pratica
#O arquivo  numero.txt contem numeros inteiros, um numeros por linha  o 
#conteudo pode ser parecido com este:
#Escreva uma funçao chamada Maior, que leia o arquivo e retorne o maior 
#numero do arquivo.
#Observe que a função nao recebe argumentos o arquivo com o qual voce esta
#trabalhando é sempre nomeado numeros.txt
#def maior ():
try:
    def numeros():
        with open("numeros.txt") as arquivo:
            maior = 0
            for linha in arquivo:
                numero = int(linha)
                if numero > maior:
                    maior = numero
            print ("maior numero ",maior)
except FileNotFoundError:
    print("erro arquivo")
except ValueError:
    print("erro o arquivo contem dados que nao sao numeros")
numeros()


"""
def Maior():
    try:
        with open("numeros.txt", "r") as arquivo:
            numeros = [int(linha.strip()) for linha in arquivo]
        return max(numeros)
    except FileNotFoundError:
        print("O arquivo 'numeros.txt' não foi encontrado.")
    except ValueError:
        print("O arquivo contém valores inválidos.")

# Exemplo de uso
maior_numero = Maior()
if maior_numero is not None:
    print(f"O maior número do arquivo é: {maior_numero}")


#manipular arquivos 
conteudo = None
try:
    with open("exemplo.txt") as novo_arquivo:
        #conteudo = novo_arquivo.read()
        #print(conteudo)
        for linha in novo_arquivo:
            print(linha)
except FileNotFoundError:
    print("Não encontramos o arquivos")


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
