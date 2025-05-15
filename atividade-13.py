#atividade 13 perimetro
#crie um progrma eque solicite ao usuairo a largura  e a altura de um retangulo, calcule a area 
#(largura * altura) e o perimetro (2*(lagura + altura)). e imprima os resultados 

largura = float(input("Informe Largura = "))
altura = float(input("informe a altura = "))
area = largura * altura
perimetro = (2* (largura+altura))

#soma_numeros = (numero_1+numero_2 + numero_3) / 3

print(f"largura = {largura:.2f} \naltura = {altura:.2f}  \narea = {area}\nperimetro = {perimetro:.2f}")
