#atividade 10
#lista interativa de compras
#implemente  uma funçao chamada lista_compras() que :
<<<<<<< HEAD
 
=======

>>>>>>> d5ccbe75886ffa8889d8efbaa7e782a7508698fe
#Use while para permitir ao usuario adicionar itens a lista;
#remova itens se o usuario digitar remover:<item>;
#termine quando o usuario digitar remover:<item>;
#termine quando o usuario digitar sair;
#Mostre a lista final organizada em ordem alfabetica.
lista_compra=["pão","arros","picanha","alcatra","bacalhau"]
#def lista_compras():
<<<<<<< HEAD
#listas=[]
lista=str(input("Digite item para lista = "))
lista.append(lista_compra)
=======
listas=[]
lista=input("Digite item para lista = ")
listas.append(lista_compra)
>>>>>>> d5ccbe75886ffa8889d8efbaa7e782a7508698fe
while True:
    if lista==("remover"):
        remo_item=input("Informe item para remover = ")
        del lista_compra[remo_item]
<<<<<<< HEAD
    else:
        if lista=="sair":
            break
        else:
            listas.append(lista_compra)
            print(lista_compra)
            break
 
=======
    else: 
        if lista=="sair":
            break
        else:
            listas.append(lista_compra) 
            print(lista_compra)
            break

>>>>>>> d5ccbe75886ffa8889d8efbaa7e782a7508698fe
"""
def lista_Crescente():
    numeros=[]
    while True:
        numero=int(input("digite um numero: "))
        numeros.append(numero)
        if len(numeros) >1 and numeros[-1] < numeros[-2]:
            break
    numeros_ordenados = sorted(numeros)
    print("numeros digitados (ordem crescente):",numeros_ordenados)
lista_Crescente()
"""
<<<<<<< HEAD
 
 
=======
>>>>>>> d5ccbe75886ffa8889d8efbaa7e782a7508698fe
