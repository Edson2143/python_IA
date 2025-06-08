""" #Aqui é uma variável nome
#A variável tem 3 elementos
#rotulo (nome), valor e tipo de dado ( no Python é dinamico a tipagem)
nome = "John" 
sobrenome = "Ramalho"

print("Meu nome", nome ,"e meu sobre nome é", sobrenome)
# input é uma entrada de dados. Solicita ao usuário um dado para continuar a execução do programa
nome = input("Qual seu nome? ")
print("Olá ", nome)

#Impressão de Strings
print(nome) #simples

print(f"Meu nome é {nome}") #f de format

print("Meu nome é: {}, meu sobrenome é {}".format(nome,sobrenome)) #format ao final """


#variaveis
nome = "Luiz"
idade = 20
skill1 = "Python"
level1 = "Iniciante"
skill2 = "Java"
level2 = "senior"
skill3 = "C++"
level3 = "Pleno"
baixo = 2000
alto = 3000
media = (baixo + alto) / 2

print(f"Meu nome é {nome} tenho {idade} anos \n \n minhas  habilidades são \n - {skill1} ({level1}) \n - {skill2} ({level2}) \n - {skill3} ({level3}) \n \n Procuro um emprego com um salário de {baixo} a {alto} euros por mês");

