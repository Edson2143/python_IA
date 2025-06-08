with open("atividades/arquivos/pessoas.csv") as novo_arquivo:
    for linha in novo_arquivo:
        linha = linha.replace("\n","")
        partes = linha.split(";")
        nome = partes[0]
        notas = partes[1:]
        print("Nome: ", nome)
        print("Nota: ", notas)
        