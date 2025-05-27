#atividadefuncao10
#Por favor escreva uma funçao chamada mesmo_caracter, que recebe uma string e dois 
# inteiros como agumentos. os inteiros se referem a indicies dentro da string a funçao
#  DEVE RETORNA TRUE SE OS DOIS CARACTERS NOS INDICES ESPECIFICADOS FOREM OS MESMOS. 
# CASO CONTRARIO E ESPECIALMENTE SE QUALQUER UM DOS INDICES ESTIVER FORA DO ESCOPO 
#  .DA STRING,A FUNÇAO RETONA False

def mesmo_caracter(string, indice1,indice2):
#testar se indice esta na faixa intervalo
    if 0 <= indice1 < len(string) and 0 <= indice2 < len(string):
        return string[indice1] == string[indice2]
    else:
        print("o indices não conferem")
print(mesmo_caracter("abacaxi", 0, 5))  # False (caracteres: 'a' e 'x')
print(mesmo_caracter("abacaxi", 0, 2))  # True (caracteres: 'a' e 'a')
print(mesmo_caracter("abacaxi", -1, 2)) # False (índice -1 está fora do escopo)
print(mesmo_caracter("zbacaxiqopz", 0, 10)) # False (índice 10 está fora do escopo)

print (mesmo_caracter("EdsonMoreira",1,5))
def mesmo_caracter(string, indice1, indice2):
    # Verifica se os índices estão dentro do escopo da string
    if indice1 < 0 or indice2 < 0 or indice1 >= len(string) or indice2 >= len(string):
        return False
    # Retorna True se os caracteres nos índices forem iguais, caso contrário, False
    return string[indice1] == string[indice2]


print(mesmo_caracter("abacaxi", 0, 4))  # False (caracteres: 'a' e 'x')
print(mesmo_caracter("abacaxi", 0, 2))  # True (caracteres: 'a' e 'a')
print(mesmo_caracter("abacaxi", -1, 2)) # False (índice -1 está fora do escopo)
print(mesmo_caracter("zbacaxiqopz", 0, 10)) # False (índice 10 está fora do escopo)

"""
def mesmo_caracter(string, indice1,indice2):
#testar se indice esta na faixa intervalo
    if 0 <= indice1 < len(string) and 0 <= indice2 < len(string):
        return string[indice1] == string[indice2]
    else:
        print("o indices não conferem")

print (mesmo_caracter("EdsonMoreira",1,5))



Essa função é simples, eficiente e cobre os casos mencionados. 😊

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