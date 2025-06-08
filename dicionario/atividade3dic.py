#Atividade 3
#escreva uma funçao chamada invert(dicionario: dict), que recebe um dicionairo
#como argumento. O dicionario deve ser invertido no lugar para que valores se
#tornem chaves e CHAVES SE TORNEM VALORES
#dict_original = {'a': 1, 'b': 2, 'c': 3}

# Invertendo o dicionário
dict_invertido = {valor: chave for chave, valor in dict_original.items()}

print(dict_invertido)
# Saída: {1: 'a', 2: 'b', 3: 'c'}


#atividade 3
def invert(dicionario: dict):
    # Cria um dicionário vazio para armazenar o resultado invertido
    invertido = {}
   
    # Percorre cada par chave-valor do dicionário recebido
    for chave, valor in dicionario.items():  # .items() permite acessar chave e valor
        # Inverte: valor vira chave, chave vira valor
        invertido[valor] = chave
   
    # Retorna o dicionário invertido
    return invertido
 
# Cria um dicionário com dados de uma pessoa
Pessoa = {"nome": "Ariel", "altura": 150, "peso": 70, "idade": 18}
 
# Exibe o dicionário original
print("Dicionário original:")
print(Pessoa)
 
# Chama a função para inverter e armazena o resultado em uma variável
invertido = invert(Pessoa)
 
# Exibe o dicionário invertido
print("Dicionário invertido:")
print(invertido)
 
 


