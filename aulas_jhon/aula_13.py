#Deletando chaves
#del
staff = {"Alan":"Professor","Emily":"Aluna","Davi":"Professor"}

# print(staff)

del staff["Alan"]
# print(staff)

#Pop
#Pop armazena o valor deletado, podemos gravar em uma variável
deletado = staff.pop("Emily")
# print(deletado)

#Estruturar dados com Dicionário
Pessoa1 = {"nome":"Peppa Pig","Altura":135,"Peso":105,"idade":14}
Pessoa2 = {"nome":"Lilo Stitch","Altura":50,"Peso":40,"idade":200}
Pessoa3 = {"nome":"Ariel","Altura":175,"Peso":200,"idade":15}

Pessoas = [Pessoa1, Pessoa2, Pessoa3]

for pessoa in Pessoas:
    print(f"Nome: {pessoa["nome"]}")
    print(f"Idade: {pessoa["idade"]}")
    print(f"Altura: {pessoa["Altura"]}")
    print(f"Peso: {pessoa["Peso"]}")
    print(" ")
    
altura_combinada = 0

for pessoa in Pessoas:
    altura_combinada += pessoa["Altura"]

print(altura_combinada)
    


