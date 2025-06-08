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
#

      
