#Atividade 4
# Escreva uma função chamada add_filme(database: list, nome: str, diretor: str, ano: int,duracao: int),
# que adiciona um novo objeto de filme em um banco de dados de filmes. O banco de dados é uma lista,
# e cada objeto de filme na lista é um dicionário. O dicionário deve conter as seguintes chaves:
# nome
# diretor
# ano
# tempo de execução
# Os valores anexados a essas chaves são fornecidos como argumentos para a função
def add_filme(database,nome,diretor,ano,duracao):
    filme = {
    "nome": nome,
    "diretor ": diretor,
    "ano ": ano,
    "duração ": duracao
    }
    database.append(filme)


banco_de_dados = []
add_filme(banco_de_dados, "Inception", "Christopher Nolan", 2000, 150)
add_filme(banco_de_dados, "Parasite", "Bong Joon-ho", 2019, 132)

print(banco_de_dados)



