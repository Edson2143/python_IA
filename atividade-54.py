#atividade54
#escreva um programa  que solicite ao usuario para digitar duas palavras. o programa deve continuar 
# pedido até que ambas as palavras tenham a mesma quantidade de caracteres

import random
palavra1 = input("Digite uma palavra1 = ")
palavra2 = input("Digite outra palavra2 = ")
caracterplavra1 = 0
caracterplavra2 = 0
#print (f"saldodisponivel = {valorsaque}")

while True:
     if len(palavra1) == len(palavra2):
         print("contagem igual")
         print(len(palavra1) == len(palavra2))
         break
     else:
       print(len(palavra1) == len(palavra2))
       palavra1 = input("Digite uma palavra = ")
       palavra2 = input("Digite outra palavra = ")
      


