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
adicionar_entrada_diario()
