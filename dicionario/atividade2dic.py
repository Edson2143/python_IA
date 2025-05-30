#atividade 2
#Escreva uma versao melhorada  do  aplicativo de lista telefoneica. 
#cada entrada agora adeve acomadar varios numeros de telefone o aplicativo 
#deve funcionar exatamente como acima. mas desta vez todos os numeros 
#anexados a um  noma devem ser impressos

def lista_telefonica():
    agenda = {}  
 
    while True:
        comando = input("Comando (1 busca, 2 adiciona, 3 sai): ")
 
        if comando == "1":
            nome = input("nome: ")
            if nome in agenda:
                print("número:", agenda[nome])
                i = 0
                while i < len(agenda[nome]):
                    i += 1
            else:
                print("nenhum número")
 
        elif comando == "2":
            nome = input("nome: ")
            numero = input("número: ")
            if nome in agenda:
                agenda[nome].append(numero)
            else:
                agenda[nome]=[numero]
            print("ok!")
        elif comando == "3":
            print("saindo...")
            print(agenda)
            break
        else:
            print("Comando inválido. Tente novamente.")          
lista_telefonica()


"""
def lista_telefonica():
    agenda = {}  
 
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
            lista_vazia=[numero]
            print("ok!")
        elif comando == "3":
            print("saindo...")
            print(agenda)
            break
        else:
            print("Comando inválido. Tente novamente.")          
lista_telefonica()
lista_vazia=[]
"""