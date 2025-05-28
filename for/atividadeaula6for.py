#escreva uma funcção chamada sem_vogal, que recebe um argumento string. 
# a funçao retorna uma nova string. que deve ser a mesma que a original, 
# mas com todas as vogais removidas.
#Voce pode assumir que a seguqencia contera apenas caraceres do alfabeto 
#ingles minusculo de a a z.
#minha_string = "Ola amigos, de rede globo, gique ligado que vi passar seçao da tarde"
import re



#lista0=[]
def sem_vogal(texto):
    vogais = "(aeiou"
    nova_string=""
    for letra in texto:
        if letra not in sem_vogal:
            nova_string += letra
    return nova_string
print(sem_vogal("Ola amigos, de rede globo, gique ligado que vi passar seçao da tarde"))

CORRIGIR 