#atividade 1
#escreva um aplicativo de lista telefonica. ele deve funionar da seguinte 
#forma:
#comando(1 busca, 2 adiciona, 3 sai): 2
#Lista telefônica
def lista_telefonica():
    agenda = {} #dicionario 
    while True:
        comando = input("Comando (1 busca, 2 adiciona, 3 sai): ")
        if comando == "1":
            nome = input("nome: ")
            if nome in agenda:
                print("número:", agenda[nome])
            else:
                print("nenhum número")
        elif comando == "2":
            nome = input("nome: ")
            numero = input("número: ")
            agenda[nome] = numero
            print("ok!")
        elif comando == "3":
            print("saindo...")
            print(agenda)
            break
        else:
            print("Comando inválido. Tente novamente.")          
lista_telefonica()
""" 
print("1 busca ")
print("2 adiciona ")
print("3 sai ")
opcao = int(input("Digite opcao "))
def lista_tel(texto):
    telefonica={}
    if opcao == 1:
        nome=input("Digite o nome = ")
        for nome in texto:
            print(nome)
            telefonica[nome] +=1
    else:
        if opcao == 2:
            print(telefonica)    

lista_tel("joao")
"""