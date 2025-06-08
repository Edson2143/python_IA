
import numpy as np
# Criando o gerador de números aleatórios com os mesmos numeros
#rng = np.random.default_rng(seed=42)
# Criando o gerador de números aleatórios
rng =np.random.default_rng()
#np.ones
#cria um array preenchido por zeros
#atividade 1
#criar arrey a partir de lista
#Escreva uma funçao chamada criar_array que receba uma lista de numeros inteiros
#e retorne um array Numpy
def criar_array(lista):
    return np.array(lista)
numeros =[15,6,8,9,1]
#array_num = criar_array(nomeros)
print(criar_array(numeros))

one_array=np.ones((2,5),dtype=int)
print(one_array)
#np.full
#cria um array preenchido com numeros especificos
full_array=np.full((2,3),8.1)
print(full_array)

#np_arrange
array_arrange=np.arange(0,10,2)
print(array_arrange)
#0, 5, 0.5
array_float_arange = np.arange(0,5,0.5)
print(array_float_arange)

#array de nueros aleatorios
array_aleatoriaos = rng.random((2,5))
array_aleatoriaos_inteiros = rng.integers(1, 10, size=(2, 5)) 
print(array_aleatoriaos)
print(array_aleatoriaos_inteiros)
# Escolher um item aleatório de uma lista
import random as ra
lista = ['maçã', 'banana', 'laranja', 'uva']
item_aleatorio = ra.choice(lista)
print(f"Item aleatório da lista: {item_aleatorio}")


#array indice numpy
array_indice = np.array((1,2,5,9,8))
print(f"eleento 0: {array_indice[0]}")
print(f"eleento 0: {array_indice[3]}")

array_indice2 = np.array([[1,2,5,9,8],[5,9,8,7,6]])
print(f"eleento 0: coluna 2 = {array_indice2[0,2]}")

arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 12, 13],
                  [14, 7, 15, 16]])
fatia2d_a=arr2d[:3,1:3]
print(fatia2d_a)

#operaçoes matematicas em python
array_a = np.array([1,3,5,8])
array_b = np.array([2,3,4,5])
soma=array_a +array_b
print(f"soma: = {soma}")
#subtracao
menos=array_a-array_b
print(f"subtração: = {menos}")
#divisao
divisao=array_a/array_b
print(f"divisão: = {divisao}")


#Copy e view
precos =np.array([180.00,10.00,20.50])
print(f"preços : {precos}")
precosajustado = precos
print(f"preço X2: = {precos[0] *2}")

precosajustado = precos.view()
print(f"view: = {precosajustado}")


precosajustado2 = precos.copy()
print(f"Ajustado: = {precosajustado2}")

#interacao
array = np.array([1,2,3,4,5,6,7,8,9,1,25,35])
for n in array:
    print(f"valor: = {n}")

#tuplas
#imutavei
#np.array converte tuplas e listas em array (arranjo)
tupla=(1,2,3,4,5,6,7,8,9,10)
array_tupla =np.array(tupla)
print(f"tirou as vigulas: = {array_tupla}")
#np;zeros
#cria um array preenchidos por zeros
zero_array = np.zeros((2,3),int)
print (f"array de zero duas linhas 3 colunas : \n {zero_array}")                       

#criar array de listas e tuplas
lista_py=[1,2,3,4,5,6]
print(f"print lista com virgulas: {lista_py}")
array_1d=np.array(lista_py)
print(f"print tupla sem virgulas: {array_1d}")

lista2_py=[[1,2,3,4],[1,2,3,4]]
array_2d=np.array(lista2_py)
print(array_2d)

arr1d = np.array([0,1,2,3,6])
print(f"criar array D1: {arr1d}, Dimensoes:{arr1d.ndim}")
print(f"shape do arr1d: {arr1d.shape}")
print(f"size do arr1d: {arr1d.size}")
print(f"dtype do arr1d: {arr1d.dtype}")
print(f"itemsize do arr1d: {arr1d.itemsize}")

arr2d = np.array([[2.5,1],[2.5,3],[2.5,3],[10.5,11]])
print(f"criar array D2: {arr2d}, Dimensoes:{arr2d.ndim}")
print(f"shape do arr2d: {arr2d.shape}")
print(f"size do arr2d: {arr2d.size}")
print(f"dtype do arr2d: {arr2d.dtype}")
print(f"itemsize do arr2d: {arr2d.itemsize}")


import numpy as np
arr1d = np.array ([1,2,3])
#funçao : arr1d.ndim funçao do python
print(f"Array D1:{arr1d}, Dimensoes:{arr1d.ndim}")

#criando arr2d
arr2d= np.array([[1, 2, 3,4,5],[5,6,8,9,6]])
# Acessando elementos
print(f"Arry D2: {arr2d}, dimenspes:{arr2d.ndim}")

arr3d= np.array([[[1, 2, 3],[4, 5, 6],[7, 8, 9],[5,9,8]]])
print(f"arry 3D: {arr3d},dimensoes: {arr3d.ndim}")

#shape
#indica o tamanho do array
print(f"shape do arr1d: {arr1d.shape}")
print(f"shape do arr2d: {arr2d.shape}")
print(f"shape do arr3d: {arr3d.shape}")

#Dtype
array_float = np.array({1.5,1,8,9,5})
print(f"o dtypedessa array é: {array_float.dtype}")
print(f"O dtype da arr1d é: {arr1d.dtype}")

#Itemsize
print(f"o edessa Itemsize arr1d é: {arr1d.itemsize}")
print(f"O dtype da Itemsize arr3d é: {arr3d.itemsize}")
print(f"O dtype da Itemsize array_float é: {array_float.itemsize}")
    
