#escreva um progrma que solicite o preço  de um produto e o precentual de desconto, calcule o valor do desconto e novo preço, e imprima os resultados.
preco = float(input("digite o preço "))
desconto= float(input("digite o desconto "))
valor_desconto=(preco*desconto / 100)

print (f"produto = {preco} percentual descoto= {desconto} valor do desconto = {valor_desconto} novo preco = {preco-desconto}")


