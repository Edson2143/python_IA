#atividadefuncao9
#Por favor, escreva ua funçaochamadao maior_numero, que recebe tres argumentos. 
#a funçao retorna o maior valor dos três
def o_maior_numero(x,y,z):
    maior = x
    if x > maior:
        maior= y
    if z > maior:
        maior = z
    return maior
def o_maior_numero2(x,y,z):
    return max(x,y,z)

print(o_maior_numero(10,20,30))
print(o_maior_numero2(50,14,90))    





"""
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

def trinangulo(x):
    contador = 0
    while contador < x:
        elementos = "*" * (contador + 1)
        print(elementos)
        contador += 1
trinangulo(5)
# imprimir valor invertido
def trinangulo(x):
    contador = 0
    while contador < x:
        elementos = "*" * (x - contador)
        print(elementos)
        contador += 1
trinangulo(5)
"""