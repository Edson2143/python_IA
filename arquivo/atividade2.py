#atividade 2
#Crie um progrma em python que peça ao usuario para digitar um texto e salve 
#esse testo em um arquivo chamado "saida.txt". Se o arquivo não existir, 
#ele deve ser criado.

texto = input("Digite um titulo: ")
nome_arquivo = "dados2.txt"

with open(nome_arquivo,"w") as arquivo:
    arquivo.write(texto)

print(f"Texto salvo com sucesso em '{nome_arquivo}'!")


"""
with open("dados2.txt","x") as arquivo:
    f = arquivo
    f.write("\nNova linha, jesus")
    #print (f(1))

# Solicita ao usuário que digite um texto
texto = input("Digite um texto: ")

# Nome do arquivo onde o texto será salvo
nome_arquivo = "saida.txt"

# Abre o arquivo em modo de escrita ('w') e salva o texto
with open(nome_arquivo, "w") as arquivo:
    arquivo.write(texto)

print(f"Texto salvo com sucesso em '{nome_arquivo}'!")
"""

