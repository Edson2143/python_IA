#atividade 4
#Crie um programa que leia um arquivo de texto chamado "texto.txt" e conte 
#quant linhas ele contem. Ao final, exiba o numero de linhas
try:
    with open("texto.txt",'r', encoding='utf-8') as arquivo:
        total=0
        for linha in arquivo:
            linha=linha.replace("\n","")
            total +=1
        print(f"total linha",total)
except FileNotFoundError:
    print("arquivo não existe")


"""
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

