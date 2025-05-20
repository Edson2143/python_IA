#Atividade 7 escreva uma funçao chamada caixa_de_hashtag, que imprima um retangulo de 
#caracteres hash. a funçao recebe um argumento, que especifica a altura do retangulo. 
#o retangulo deve ter dez caracteres de largura.
#a funçao deve chamar a funçao linha do exercicico anteriror para a impressao real.
#copie a sua soluçao para esse exercicico acima do codigo para este exercicio. 
#por favor naoaltere nada em sua funçao linha.
def linha(n,texto):
    if texto =="":
        caractere = '*'
    else:
        caractere = texto[0]
    print(caractere * n)


def caixa_de_hashtag(altura):
    contador = 0
    while contador < altura:
        linha(10, "#")
        contador += 1

caixa_de_hashtag(7)
