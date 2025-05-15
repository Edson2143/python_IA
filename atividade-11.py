#atividade 11juros simples
#crie um progrma eque solicite ao usuairo o capital inicial, a taxa de juros anual e o tempo em anos , 
#calcule os juros simples(Juros = Captial * Tempo) e imprimima o monteante final

capital_inicial = float(input("Capital Inicial ? ")) #1000
taxa_juros_anual = float(input("Taxa juro anual ? ")) #12%
tempo_em_anos = float(input("Tempo em anos ? "))
juros_simples = capital_inicial * (taxa_juros_anual / 100) * tempo_em_anos 

montante = capital_inicial  + juros_simples
print(f"Juros_simples = {juros_simples} Montante = {montante}")
