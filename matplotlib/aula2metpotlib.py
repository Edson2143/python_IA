
import matplotlib.pyplot as plt
import numpy as np
#crando uma  series
x=np.linspace(0,10,100)
#usando metodo de seno do numpy
y_line = np.sin(x)
categorias =['Ação','comedia','dra,a','terror']
valores = [20,40,50,20]
x_scatter=np.random.rand(50)
y_scatter=x_scatter+np.random.randn(50)*0.1

#hitograma
hist_data=np.random.randn(1000)

fig,axs = plt.subplots(2,2, figsize=(10,8))
axs[0,0].plot(x,y_line,color='blue',linestyle='--',
label='sin(x)')

axs[0,0].set_title('Grfico de linha')
axs[0,0].legend()

axs[0,1].bar(categorias,valores,color=['green','red','blue','purple'])
axs[0,1].set_title('grafico debarras')


axs[1,0].scatter(x_scatter,y_scatter,alpha=0.6,color='red')
axs[1,0].set_title('grafico de dispersao')

axs[1,1].hist(hist_data,bins=30,color='blue',edgecolor='black')
axs[1,1].set_title('Histograma')
fig.get_tight_layout()
plt.show()