
import numpy as np
#atividade 7
#Escreva uma funçao chamada somar_matrizes que receba uas matrizes do mesmo 
#tamanho e retorne a soma delas. se não forem do mesmo tamnho, a função deve 
#retornar uma mensagem de erro.
def somar_matrizes(matriz1,matriz2):
    if np.shape(matriz1) == np.shape(matriz2):
        return matriz1 + matriz2
    else:
        return "Erro as matrizes devem ter o mesmo tamanho."
n1 = np.array([[1,3,5,8],[6,5,8,4]])
n2 = np.array([[2,3,4,5],[9,8,7,9]])
print (somar_matrizes(n1,n2))

"""
if len(linha1_a) == len(linha2_b) and len(linha3_c):
    soma=linha1_a + linha2_b + linha3_c
    print(soma)
else:
    print("erro")

linha1_a = np.array([1,3,5,8])
linha2_b = np.array([2,3,4,5])
linha3_c = np.array([10,11,14,15])    

numeros = [10, 20, 30, 40, 50]

def estatisticas_array(arr):
    if not arr: #checa lista vazia
        return {"soma": 0, "media": 0}  # Retorna valores padrão para lista vazia
    
    soma = sum(arr)
    media = soma / len(arr)
    
    return {"soma": soma, "media": media}
# Exemplo de uso:
resultado = estatisticas_array(numeros)
print(resultado)  # Saída: {'soma': 150, 'media': 30.0}

# atividade 4
# gerar array de valores entre dois numeros

#escreva um afunçao chamada gerar_array_intervalo que receba dois inteiros e 
#retorne uma array contendo todos os inteiros

def gerar_array_intervalo(inicio,fim):
    if inicio <= fim:
        return np.arange(inicio,fim +1)
    
print(gerar_array_intervalo (3,7))


one_array=np.ones((2,3),int)
print(one_array)
#np.pfull
#cria um array preenchido com numeros especificos
full_array=np.full((2,3),7.5)
print(full_array)

#np_arrange
array_arrange=np.arange(0,10,2)
print(array_arrange)

array_float_arange = np.arange(0.0,1.0,0.25)
print(array_float_arange)
#array de nueros aleatorios
array_aleatoriaos = rng.random((2,5))
array_aleatoriaos_inteiros = rng.integers(1, 10, size=(2, 5)) 
print(array_aleatoriaos)
print(array_aleatoriaos_inteiros)

#array indice numpy
array_indice = np.array((1,2,5,9,8))
print(f"eleento 0: {array_indice[0]}")
print(f"eleento 0: {array_indice[3]}")

array_indice2 = np.array([[1,2,5,9,8],[5,9,8,7,6]])
print(f"eleento 0: coluna 2 {array_indice2[0,2]}")

arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 12, 13],
                  [14, 7, 15, 16]])
fatia2d_a=arr2d[:3,1:3]
print(fatia2d_a)

#operaçoes matematicas em python
array_a = np.array([1,3,5,8])
array_b = np.array([2,3,4,5])
soma=array_a +array_b
print(soma)
#subtracao
menos=array_a-array_b
print(menos)
#divisao
divisao=array_a/array_b
print(divisao)

#Copy e view
precos =np.array([180.00,10.00,20.50])
print(f"preços : {precos}")
precosajustado = precos
print(precos[0] *2)
precosajustado = precos.view
print(f"view: {precosajustado}")

precosajustado2 = precos.copy()
print(precosajustado2)

#interacao
array = np.array([1,2,3,4,5,6,7,8,9,1,25,35])
for n in array:
    print(f"valor:{n}")

#tuplas
#imutavei
#np.array converte tuplas e listas em array (arranjo)
tupla=(1,2,3,4,5,6,7,8,9,10)
array_tupla =np.array(tupla)
print(array_tupla)
#np;zeros
#cria um array preenchidos por zeros
zero_array = np.zeros((2,3),int)
print (f"array de zero: \n {zero_array}")                       

#criar array de listas e tuplas
lista_py=[1,2,3,4,5,6]
print(lista_py)
array_1d=np.array(lista_py)
print(array_1d)

lista2_py=[[1,2,3,4],[1,2,3,4]]
array_2d=np.array(lista2_py)
print(array_2d)


arr1d = np.array([0,1,2,3,6])
print(f"criar array D1: {arr1d}, Dimensoes:{arr1d.ndim}")
print(f"shape do arr1d: {arr1d.shape}")
print(f"size do arr1d: {arr1d.size}")
print(f"dtype do arr1d: {arr1d.dtype}")
print(f"itemsize do arr1d: {arr1d.itemsize}")

arr2d = np.array(
    [[2.5,1],[2.5,3]],
    [[2.5,3],[10.5,11]])
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
"""

      
