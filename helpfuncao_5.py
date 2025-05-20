#1. Definição da função:
#A função quadrado_string recebe dois argumentos: texto (uma string) e tamanho (um inteiro).
#2. Loop de repetição:
#O loop for i in range(tamanho) itera sobre cada linha do quadrado.
#3. Impressão da linha superior:
#A linha print(texto[i:i+tamanho]) imprime uma parte da string texto, que corresponde a uma linha do quadrado.
#4. Impressão da linha inferior:
#A linha print(texto[tamanho - (tamanho - i) : tamanho - 1]) imprime outra parte da string texto, formando a linha inferior do quadrado.
#5. Exemplo de uso:
#A chamada quadrado_string("aybabtu", 5) imprime o quadrado conforme o exemplo fornecido.

#Recebe uma string e um inteiro e imprime um quadrado de caracteres.
"""
Args:
   texto: #A string a ser utilizada.
   tamanho: #O tamanho do lado do quadrado.

Returns:
    None. Imprime o quadrado de caracteres no terminal.
"""
def quadrado_string(texto, tamanho):

   for i in range(tamanho):
      print(texto[i:i+tamanho])
      print(texto[tamanho - (tamanho - i) : tamanho - 1])

tamanho = 10
texto = "edson"



