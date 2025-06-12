
import matplotlib.pyplot as plt
import numpy as np
#crando uma  series
x2 = [1,2,3,5,6]
y = [2,5,6,8,6]

plt.plot(x2,y)
plt.title('Exemplo de linha')
plt.xlabel('eixo x')
plt.show()

#grafico de barra
categorias=['A','B','C']
valores=[10,2,30]
plt.bar(categorias,valores)

#de linha
plt.bar(categorias,valores)
plt.title('Barras')
plt.show()

#graficos de pizza
plt.pie(valores,labels=categorias,autopct='%10.2f%%')
plt.title('Pizza')
plt.show()

#histogrma
dados= np.random.randn(1000)
plt.hist(dados,bins=30)
plt.title('Histograma')
plt.show()

#Disperçao
x=np.random.rand(50)
y=x+np.random.rand(50)*0.1
plt.scatter(x,y)
plt.title("Dispersao")
plt.show

