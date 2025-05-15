#atividade53
#Crie um programa que simule um caixa eletronico. o programa deve pedir ao usuario para inserir um valor de saque que deve ser multiplo de 10 
#e nao pode exceder o slado disponivel. continue pedindo ate que o valor inserido seja valido.

import random
informevalor = 0
valorsaque = 0
saldodisponivel = 500
print (f"saldodisponivel = {valorsaque}")

while True:
    saque = 
    if valorsaque % 10 != 0:
        print ( "o valor dec ser multiplode 10")
    elif valorsaque > saldodisponivel
        print ("saldo insufi")
    elif saldodisponivel <= 0:
        print ("valor invalido")
    else:
        saldodisponivel -= valorsaque
        print(f"saque de R$ {valorsaque} realizado sucesso!")
        print(f"Saldo restate : R$ {saldodisponivel}")

    