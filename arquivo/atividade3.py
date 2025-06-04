#atividade 3
#Escreva um programa em python que abra um arquivo  chama "entrada.txt" 
#(supondo queja exista no mesmo diretorio) e imprima tudo o seu conteudo 
#no terminal.
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


"""
texto = input("Digite um titulo: ")
nome_arquivo = "dados2.txt"

with open(nome_arquivo,"w") as arquivo:
    arquivo.write(texto)

print(f"Texto salvo com sucesso em '{nome_arquivo}'!")
"""

