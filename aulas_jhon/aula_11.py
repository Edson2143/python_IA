#count() - conta quqantas vezes uma string ou inteiro tem dentro de um conjunto den dados
minha_string = "Quantas madeiras um esquilo poderia empilhar se um esquilo pudesse empilhar madeiras"
print(minha_string.count("a"))

minha_lista = [1,2,3,5,6,6,9,9,8]
print(minha_lista.count(6))


#Replace
minha_palavra = "Oi, Oi, oi, amigos"
nova_palavra = minha_palavra.replace("Oi", "Olá")
print(nova_palavra)

num = str([0,20,30,5,60,9,4,7])
novo_num = num.replace("0","5")
print(list(novo_num))


