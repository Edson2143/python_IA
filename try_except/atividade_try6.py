#atividade 6
#ecolha 3 except que voce ainda não usou nas ativiades anteriores e tente
#aplicar em um codigo
# RuntimeError
# StopIteration "um iterador chegou ao fim" next(iter([]))

"""
my_dict = {"name": "Alice", "age": 25}

address = my_dict.get("address", "No address available")
print(address)  # Output: No address available

my_dict = {"name": "Alice", "age": 25}
try:
    print(my_dict["address"])
except KeyError:
    print("Key 'address' not found!")

try:
    class Cachorro:
        def latir(self):
            print("Au au!")

    dog = Cachorro()
    dog.miar()  # Isso causará um AttributeError
except AttributeError:
    print ("erro Atrrib error ")

try:
    def verificar_valor(valor):
        if valor < 0:
            raise RuntimeError("Valor não pode ser negativo!")
        return valor

# Testando a função
    print(verificar_valor(10))  # Funciona normalmente
    print(verificar_valor(-5))  # Gera RuntimeError

except RuntimeError:
    print ("erro Run")

try:
    def meu_gerador():
        yield 2
        yield 3
        yield 3
    gen = meu_gerador()

    print(next(gen))  # 1
    print(next(gen))  # 2
    print(next(gen))  # 3
    print(next(gen))  # StopIteration ocorre aqui!
except StopIteration:
    print("erro stopiteration")

#atividad 5
#crie um programa que:
#peça ao usuario para diiitar um numero divisor e um indice para acessar em uma lista
#a lista deve ter 3 numeros
#Use try except para capturar divisao por zero, indice invalido e qualquer 
#outro erro generico.
lista=[3,4,5]
try:
    digite_numero = int(input("Informe o Numero: = "))
    indice = int(input("informe um indice (0 , 2): "))
    numero = lista[indice] / digite_numero
    print(f"Resulrado da divisão: {numero}")

except ZeroDivisionError:
    print ("indice invalido")

except ValueError:
    print ("indice invalido erro")
finally:
    if numero % 2 == 0:
        print ("correto e par")
    else:
        print("não e par erro")

#atividade4
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

lista=["banana","laranja","abacate","uva"]
indice = 0
#atividade3 
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