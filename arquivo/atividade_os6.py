#atividade6
#criar uma funçao que permita ao usuario adicionar entradas em um arquivo 
#de diario diario.txt cada entrada deve contera data e uma descriçao, 
#armazenadas como dicionario antes de serem escritas no arquivo.
#importar bibliotecas para pegar data do dia

import datetime
import json

def adicionar_entrada_diario(arquivo="diario.txt"):
    # Solicita a descrição da entrada ao usuário
    descricao = input("Digite a descrição da entrada: ")
    
    # Obtém a data atual
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Cria um dicionário com a data e a descrição
    entrada = {
        "data": data_atual,
        "descricao": descricao
    }
    
    # Escreve a entrada no arquivo
    try:
        with open(arquivo, "a", encoding="utf-8") as f:
            f.write(json.dumps(entrada) + "\n")
        print("Entrada adicionada com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar entrada: {e}")

"""
import json
from datetime import datetime
def adicionar_entrada_diario():
    data= input("digite a tada: ")
    descricao = input("Digite sua entrada: ")
    entrada={"data ": data,
             "descricao": descricao
    }
    with open("diario.txt","a", encoding="utf-8") as arquivo:
        arquivo.write(str(entrada) + "\n")
    print("Entrada adicionada ocm sucesso")
adicionar_entrada_diario()

#atividade 5
#w3 scool


#criar função
def adicionar_entrada(diario_path="diario.txt"):
    #formata datatime
    data=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print()
    descricao = input("Digite sua entrada: ")
    #entrada dicionario
    entrada = {"data":data, "descricao": descricao}
    #valida erro 
    try:
        with open(diario_path,"r",encoding="utf-8") as file:
            diario = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        diario=[]
    diario.append(entrada)
    with open(diario_path,"w",encoding="urf-8") as file:
        json.dump(diario,file, indent=4,ensure_ascii=False)
    print("Entrada adicionada ocm sucesso")
#adicionar_entrada()

def adicionar_entrada(diario_path="diario.txt"):
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    descricao = input("Digite sua entrada no diário: ")
    entrada = {"data": data, "descricao": descricao}
    try:
        with open(diario_path, "r", encoding="utf-8") as file:
            diario = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        diario = []
    diario.append(entrada)
    with open(diario_path, "w", encoding="utf-8") as file:
        json.dump(diario, file, indent=4, ensure_ascii=False)
    print("Entrada adicionada com sucesso!")


import os
if os.path.exists("dados.txt"):
    print ("sim a pasta existe")
    os.rmdir("atividades/dados.txt")
else:
    print("pasta nao existe")
    os.mkdir("atovadades/dados.txt")
"""

          
             