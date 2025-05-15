palavra1 = "ex"
palavra2 = "emplo"
palavraCompleta = palavra1+palavra2
print(palavraCompleta * 5)
print("-" * len(palavraCompleta))

teste1 = input("teste1") #("pedro ")
teste2 = input("teste2 ") #("Moreira")
if len(teste1) > len(teste2):
    print(teste1)
elif len(teste1) == len(teste2):
    print (teste2)

entrada = input("Digite umtesto:  ")
print(entrada[0])
print(entrada[1])
print(entrada[2])

entrada = input("Digitie palavra")
ultimo = len(entrada) - 1
print(f" o ultimo e  {entrada[ultimo]}")