#atividade 8
#cadastro com validaçao
#crie uma funçao que peca ao usuario para cadastrar 5 senhas. Cada senha deve ter 
#pelo menos 8 caracteres e conter um numero. senhas invalidas devem  ser rejeitadas 
#com mensagem de erro. Ao final imprima todas as senhas validads.

#biblioteca para testar se tem numero em uma variavel
import re
#def senha(valor):
#    tem_letra = any(char.isalpha() for char in valor)
#    tem_numero = any(char.isdigit() for char in valor)
#    return tem_letra and tem_numero
def lista_senha(cad_senha):
    return
total_senha = 0
cad_senha = []
while True:
    senha = input("informe senha = ")
    if len(senha) >= 8 and re.search("[0-9]",senha) != None:
        total_senha +=1
        cad_senha.append(senha)
        if total_senha >= 5:
            print(cad_senha)
            print(total_senha)
            break
        else:
            print(f"menor que 5, {cad_senha}, Vezes, {total_senha}")
    else:
        print(f"menor que 8 ou não tem numero, {cad_senha},vezes,{total_senha}")
print(cad_senha)

