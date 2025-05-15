salario = int(input("qual salario?"))
horasmes = int(input("quantshoras trabalha no mes ?"))

valorhora = salario / horasmes
dia = 8
pordia = valorhora * dia
print (f"O funcionario ganha : R${valorhora} por hora")
print (f"Por dia ganha R$ {pordia}")