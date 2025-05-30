#deleta chaves
staff = {"alan":"professor","emily":"aluna","Davi":"professor"}
#print(staff)

del staff["alan"]
#print(staff)

#Pop
#Pop armazena o valor deletado, podemos gravar em uma variavel
deletado = staff.pop("emily")
#print(deletado)


#strututa dados com dicionario
pessoa1={"nome":"pappa pig","altura":195,"peso":105,"idade":15}
pessoa2={"nome":"pappa pig","altura":195,"peso":105,"idade":15}
pessoa3={"nome":"pappa pig","altura":195,"peso":105,"idade":15}

pessoas = [pessoa1,pessoa2,pessoa3]

for pessoa in pessoas:
    print(f"nome: {pessoa["nome"]}")
    print(f"idade: {pessoa["idade"]}")
    print(f"altura: {pessoa["altura"]}")
    print(f"peso: {pessoa["peso"]}")
    print(" ")

altura_combinada = 0
for pessoaa in pessoas:
    altura_combinada += pessoa["altura"]
print (altura_combinada)