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

"""
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
