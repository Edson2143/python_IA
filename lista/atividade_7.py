#atividade 7
#verifcaçao de presenca em lista
#crie uma funcao que recebe uma lista de produtos e permite que o usuario digite um
#nome. o programa deve informar se o produto esta ou nao na lista, e repetir ate o 
#usuario digirar sair
#atividade 7
#verifcaçao de presenca em lista
#crie uma funcao que recebe uma lista de produtos e permite que o usuario digite um
#nome. o programa deve informar se o produto esta ou nao na lista, e repetir ate o
#usuario digirar sair
#def lista_produto(nome_produto):
#    nome_produto = [nome_produtos]
#   return(nome_produtos

nome_l=["laranja","pera","ameixa","banana","pessego","limao"]
lista_nova=[]
lista_falsa=[]
nome_p = input("Enetre com nome inicio ")
controle = 0
while nome_p in(nome_l):
    print(f"{nome_p},Esta na lista")
    lista_nova.append(nome_p)
    nome_p = input("Enetre novo While ")
    print(f"while =,{lista_nova}")
else:
    if nome_p == "sair":
        print("fim do programa")
    else:
        lista_falsa.append(nome_p)  
        nome_p = input("Enetre com nome 0 ")
        print(lista_falsa)
        if nome_p in(nome_l):
            print(f"{nome_p},Esta na lista")
            lista_nova.append(nome_p)
            nome_p = input("Enetre novo 1 ")
        else:
            if nome_p == "sair":
                print("fim do programa")
                print(lista_nova)
            else:
                if nome_p in(nome_l):
                    print(f"{nome_p},Esta na lista")
                    lista_nova.append(nome_p)
                    nome_p = input("Enetre novo 2 ")
                    print(lista_nova)
                    if nome_p == "sair":
                        print("fim do programa")
                    else:
                        nome_p = input("Enetre novo 3 ")
                        if nome_p == "sair":
                            print("fim do programa")
                        else:
                            if nome_p in(nome_l):
                                print(f"{nome_p},Esta na lista")
                                lista_nova.append(nome_p)
                                nome_p = input("Enetre novo 4 ")
                                print(lista_nova)
                            else:
                                if nome_p == "sair":
                                    print("fim do programa")
                                else:
                                    lista_falsa.append(nome_p)
                                    nome_p = input("Enetre novo 6 ")
                                    if nome_p in(nome_l):
                                        print(f"{nome_p},Esta na lista")
                                    lista_nova.append(nome_p)
                                    nome_p = input("Enetre novo 5 ")
                                    print(lista_nova)
                                    if nome_p == "sair":
                                        print("fim do programa")

nome_l=["laranja","pera","ameixa","banana","pessego","limao"]
def verificar_presenca(nome_l):

"""
def lista_produto():
    nome_produto = []
    while nome_produto = "sair":
        colocar = str(input("Digite produto: = "))
        nome_produto.append(colocar)
        print(nome_produto)

#atividade 6
#Eliminar duplicados
#peça ao usuario para digitar 10 numero(com possibilidades de repetição). 
#Depois, crie uma nova lista contendo apenas os numeros unicos (sem repetições)
#e imprime-a
numeros_repete=[]
 #   return
controle=int(0)
while True:
        adicionar = input("Digite lista = : ")
        if controle <= 10:
            controle += 1
            if len(adicionar) <= 9:
                numeros_repete.append(adicionar)
            else:
                 #if lista_limpa.(in(insert(numeros_repete)))
                 #= list(dict.fromkeys(numeros_repete))
                 print(numeros_repete)
        else:
             print(numeros_repete)
             print("fim")

#feito pelo professor ver foto celular
def eliminar_duplicados():
     numeros = []
     while len(numeros) < 10:
        num = int(input(f"Digite o {len(numeros)+1}" numero: "))
        numeros.append(num)
unicos =[]
repetidos = []
i=0
while i < lem(numeros):
    if numeros[i] not in unicos:
        unicos.append(numeros[i]
                    )
            i= +=1
print (Unicos)
print 

#atividades 5
#menu de lista de tarefas
#Crie uma funça oque simule uma lista de tarefas com um nmenu simples
lista_adicionar=[]
lista_remover=[]
lista_mostrar=[]
#1 adiciona
#2 remover
#3 mostrar
#4 #sair
#adicionar =input("adicionar tarefa: = ")
#remover=input("Removover Tarefa: = ")
#opcao = int(input("digite opçao 1=adiciona 2=remover 3 mostrar 4 sair: ="))

opcao=""
while True:
    opcao = int(input("digite opçao 1=adiciona 2=remover 3 mostrar 4 sair: = "))
    if opcao == 1:
        #opcao = int(input("digite opçao 1=adiciona 2=remover 3 mostrar 4 sair: ="))
        adicionar =input("adicionar tarefa: = ")
        lista_adicionar.append(adicionar)
        opcao=""
    else:
        #opcao = int(input("digite opçao 1=adiciona 2=remover 3 mostrar 4 sair: ="))
        if opcao == 2:
            lista_adicionar.remove(1)
            opcao=""
        else:
            if opcao == 3:
                #opcao = int(input("digite opçao 1=adiciona 2=remover 3 mostrar 4 sair: ="))
                print(f"tarefas criadas: {lista_adicionar}")
                opcao=""
            else:
                if opcao == 4:
                    print("programa, encerrado")
                    break
                else:
                    print("opçao errrada incorrada")
                    break


#atividade4
#peça ao usuario para digitar 5 notas de alunos e armazene uma lista. Depois, 
#crie umanova lista apenas com as notas maiores ou iguais a 6 e imprimaa como 
#notas aprovadas
#def digitar():
#   return (notas)
notas=[]
opravadas=[]
while len(notas) < 5:
    nota = int(input("Informe nota "))
    notas.append(nota)
    if nota >= 6:
        opravadas.append(nota)
        #adiciona  a notaa uma nova lista se a notafor maior que 6
print(f"Notas aprovadas: {opravadas}")
      
#print(f"notas:  {aprovadas}")


#atividade 3
#escreva uma funçao que peça ao usuário para digitar 5 nomes, se o nome ja estiver na
#lista, ele na deve ser adicionado novamente. ao final imprima todos os nomes cadastrados.
nomes = ["edson","eric","jorge","marcos","jorge"]
entrada=input("Entre com um nome ")
def estiver(nomes):
    return(nomes)

print(entrada in(nomes))

lista_nomes =[]
def nomes_unicos():
    while len(lista_nomes) < 5:
        nome = input("Quqal nome " )
        if nome in(lista_nomes):
            print("nome ja existe")
        else:
            lista_nomes.append(nome)
        return lista_nomes
print(nomes_unicos)

lista_inteiro = [10,20,12,30,42,20]
lista_argumento = [1,3,4,6,7]
print(max(lista_inteiro)-(min(lista_argumento)))

valores = [8,3,15,1,9]
def diferenca_extremos(lista):
    return max(lista) - min(lista)
print(diferenca_extremos(valores))


lista = [10,25,36,65,45,98,78]
def media(lista):
    return sum(lista) / len(lista)
print(media(lista))



#Maximo , minimo a soma
lista_numeros = [0,45,78,6,32,15,7] #lista como argumento
print(max(lista_numeros))
print(min(lista_numeros))
print(sum(lista_numeros))
"""