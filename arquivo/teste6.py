import json
from datetime import datetime

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

