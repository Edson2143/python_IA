
#Arquivo :Pratica
#O arquivo  numero.txt contem numeros inteiros, um numeros por linha  o 
#conteudo pode ser parecido com este:
#Escreva uma funçao chamada Maior, que leia o arquivo e retorne o maior 
#numero do arquivo.
#Observe que a função nao recebe argumentos o arquivo com o qual voce esta
#trabalhando é sempre nomeado numeros.txt
#def maior ():
with open("pessoas.csv") as novo_arquivo:
    for linha in novo_arquivo:
        linha= linha.replace("\n","")
        partes = linha.split(";")
        nome=partes[0]
        notas=partes[1:]
        print("Nome : ",nome)
        print("notas: ", notas)
                