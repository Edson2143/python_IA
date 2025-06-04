#atividade 5
#Crie um programa que leia um arquivo csv chamado "dados.txt" que contenha 
# nomes e idades em cada linha(separados por virgula). O progrma deve criar 
# um novo arquivo chamado "dados_maiores.csv" apenas com as linhas em que a 
#idade seja maior ou igual a 18

try:
    with open("dados.csv","r", encoding="utf=8") as infile:
        reader = csv.reader(infile)
        with open('dados_maiores.csv', 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.writer(outfile)
        for linha in infile:
            conteudo = arquivo.read()
            linha=linha.replace("\n","")
            
        print(conteudo)
except FileNotFoundError:
    print("arquivo não existe")
#fazer

import csv

# Abrindo o arquivo de entrada
with open('dados.txt', 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    
    # Criando o arquivo de saída
    with open('dados_maiores.csv', 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Processando cada linha
        for linha-row in reader:
            if len(row) == 2:  # Garantir que há nome e idade
                nome, idade = row[0], row[1]
                
                try:
                    if int(idade) > 18:
                        writer.writerow([nome, idade])
                except ValueError:
                    print(f'Erro ao processar idade: {idade}')  # Evitar erros de conversão

print('Arquivo "dados_maiores.csv" criado com sucesso!')




"""
try:
    with open("texto.txt",'r', encoding='utf-8') as arquivo:
        total=0
        for linha in arquivo:
            linha=linha.replace("\n","")
            total +=1
        print(f"total linha",total)
except FileNotFoundError:
    print("arquivo não existe")


with open("pessoas.csv") as novo_arquivo:
    for linha in novo_arquivo:
        linha= linha.replace("\n","")
        partes = linha.split(";")
        nome=partes[0]
        notas=partes[1:]
        print("Nome : ",nome)
        print("notas: ", notas


try:
    # Abre o arquivo 'entrada.txt' no modo de leitura
    with open('dados2.txt', 'r', encoding='utf-8') as arquivo:
#        with open("dados2.txt","x") as arquivo:
        # Lê todo o conteúdo do arquivo
        conteudo = arquivo.read()
        # Imprime o conteúdo no terminal
        print(conteudo)
except FileNotFoundError:
    print("Erro: O arquivo 'entrada.txt' não foi encontrado no diretório atual.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")



texto = input("Digite um titulo: ")
nome_arquivo = "dados2.txt"

with open(nome_arquivo,"w") as arquivo:
    arquivo.write(texto)

print(f"Texto salvo com sucesso em '{nome_arquivo}'!")
"""

