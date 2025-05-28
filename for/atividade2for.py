
#atividades 2
#Escrevauma funçao chamada anagramas, que recebe duas strings como argumentos.
#a funçao retorna True se as string são anagrams uma das outra. Duas palavras 
#são anagrams se elas contem exateamente os mensos caracteres. Dica:
#a funçao sorted tambem pode ser usada em strings.

def  anagrama(anagramas1, anagramas2):
    return sorted(anagramas1)==sorted(anagramas2)

print(anagrama("amor", "roma")) # Verdadeiro
print(anagrama("tabby", "ybbat")) # Verdadeiro
