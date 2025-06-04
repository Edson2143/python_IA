#atividade 1
#o arquivo frutas.csv contem nomes de frutas e seus preços. escreva uma 
#funçao chamada frutas, que leis o arquivo e retorne um dicionario com 
#base no conteudo. No dicionario, o nome da fruta deve ser a chave, e o 
#valor deve ser seu preço. Os preços devem ser do tipo float.
#lista =[]
def frutas():
    lista={}
    try:
        with open("frutas.csv") as novo_frutas:
            #leitor =csv.reader(novo_frutas)
            for linha in novo_frutas:
                linha = linha.strip()
                if linha:
                    nome = linha.strip(";")
                    lista[nome[0]]=float(nome[1])
    except FileNotFoundError:
        print ("erro arquivo")
    except ValueError:
        print("erro ao converter o preço para float")
    return lista
print(frutas())

"""
import csv
def frutas():
    dicionario = {}
    # Abre o arquivo frutas.csv no modo leitura com encoding UTF-8
    with open('frutas.csv', newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        # Lê cada linha do arquivo
        for linha in leitor:
            if linha:  # Verifica se a linha não está vazia
                nome = linha[0].strip()  # Obtém o nome da fruta e remove espaços extras
                try:
                    preco = float(linha[1].strip())  # Converte o valor para float
                except ValueError:
                    # Se a conversão falhar, você pode definir um valor padrão, ou opcionalmente ignorar
                    preco = None
                dicionario[nome] = preco
        
    return dicionario

# Exemplo de uso:
if __name__ == '__main__':
    frutas_dict = frutas()
    print(frutas_dict)

lista = []
inicio = 0
quantidade = int(input("quantos numero "))
while quantidade > inicio:
    numero = int(input(f"insira um numero {inicio + 1}"))
    lista.append(numero)
    print(lista)
    inicio += 1
    print[lista]
with open("pessoas.csv") as novo_arquivo:
    for linha in novo_arquivo:
        linha= linha.replace("\n","")
        partes = linha.split(";")
        nome=partes[0]
        notas=partes[1:]
        print("Nome : ",nome)
        print("notas: ", notas
"""        
                