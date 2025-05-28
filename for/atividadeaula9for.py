#escreva uma funcção chamada mais_caracteres, que recebe um argumento string. 
# a funçao retorna o caractere que tem mais ocorrencias dentro da minha_string
minha_string = "Ola amisgos, de rede globo, gique ligado que vi passar seçao da tarde"

#lista0=[]
def mais_caracteres(texto):
    maior_caracter = ""
    maior_contagem=0
    for caracter in texto: 
        contagem = texto.count(caracter)
        if contagem > maior_contagem:
            maior_contagem=contagem
            maior_caracter=caracter
    return maior_caracter

print(mais_caracteres(minha_string.replace(" ","")))

