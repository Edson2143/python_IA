conteudo = None
try:
    with open("atividades/arquivos/exemplo.txt") as novo_arquivo:
        # conteudo = novo_arquivo.read()
        # print(conteudo)
        for linha in novo_arquivo:
            print(linha)

except FileNotFoundError:
    print("Não encontramos o arquivos")