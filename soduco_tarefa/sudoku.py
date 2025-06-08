
import numpy as np
# Criando o gerador de números aleatórios com os mesmos numeros
#rng = np.random.default_rng(seed=42)
# Criando o gerador de números aleatórios
rng =np.random.default_rng()
def eh_valido(tabuleiro, linha, coluna, num):
    for i in range(9):
        if tabuleiro[linha][i] == num or tabuleiro[i][coluna] == num:
            return False
        
    bloco_x, bloco_y = linha // 3 * 3, coluna // 3 * 3
    for i in range(3):
        for j in range(3):
            if tabuleiro[bloco_x + i][bloco_y + j] == num:
                return False
    return True

def resolver_sudoku(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                for num in range(1, 10):
                    if eh_valido(tabuleiro, linha, coluna, num):
                        tabuleiro[linha][coluna] = num
                        if resolver_sudoku(tabuleiro):
                            return True
                        tabuleiro[linha][coluna] = 0
                return False
    return True

# Exemplo de tabuleiro
tabuleiro = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if resolver_sudoku(tabuleiro):
    for linha in tabuleiro:
        print(linha)
else:
    print("Não há solução para este Sudoku.")
    
"""
sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [0, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [0, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]
"""