#escreva um progrma que solicite ao usuario o valor da conta e o percentualde gorjeta, calcuaro valor da gorjeta eo valor total a pagar, e imprima os resultados.desconto

preco = float(input("digite o preço "))
desconto= float(input("digite o desconto "))
valor_desconto=(preco*desconto / 100)

print (f"produto = {preco} \npercentual descoto= {desconto} \nvalor do desconto = {valor_desconto} \nnovo preco = {preco-desconto}")


