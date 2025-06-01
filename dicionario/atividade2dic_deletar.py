#lista telefonica - ativ 2
def lista_telefonica():
    agenda = {}
 
    while True:
        comando = input("Comando (1 busca, 2 adiciona, 3 sai): ")
        if comando == "1":
            nome = input("nome_1: ")
            if nome in agenda:
                print("números_1:")
                indice = 0
                while indice < len(agenda[nome]):
                    print(agenda[nome][indice])
                    indice += 1
            else:
                print("nenhum número")
 
        elif comando == "2":
            nome = input("nome_2: ")
            numero = input("número: ")
            if nome in agenda:
                agenda[nome].append(numero)
            else:
                agenda[nome] = [numero]
            print("ok!")
 
        elif comando == "3":
            print("saindo...")
            print(agenda)
            break
 
        else:
            print("Comando inválido. Tente novamente.")
 
lista_telefonica()
"""
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
"""