import re
import random

print(re.search("[A-Z]","Senha"))
print(re.search("[A-Z]","seNha"))
print(re.search("[A-Z]","seNha"))
print(re.search("[0-9]","seN1ha"))

numero_secreto = random.randint(1,200)
print(numero_secreto)
