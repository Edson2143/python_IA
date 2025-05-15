
valor_conta = float(input("informe o valor da conta = "))
percentual_gorjeta = float(input("informe percentual gorjeta = "))
valor_gorjeta = (valor_conta * percentual_gorjeta)/100
valor_total_pagar = (valor_conta + valor_gorjeta)
print(f"Valor Conta = {valor_conta} Percentual Gorjeta = {percentual_gorjeta} Valor Gorjeta = {valor_gorjeta} Valor Total Pagar - {valor_total_pagar}") 