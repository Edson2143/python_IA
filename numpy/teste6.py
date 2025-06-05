import numpy as np
arr1d = np.array ([1,2,3])
#funçao : arr1d.ndim funçao do python
print(f"Array 1D:{arr1d}, Dimensoes:{arr1d.ndim}")

#criando arr2d
arr2d= np.array([[1, 2, 3],[4, 5, 6]])
# Acessando elementos
print(f"Arry 2d: {arr2d}, dimenspes:{arr2d.ndim}")

arr3d= np.array([[[1, 2, 3],[4, 5, 6],[7, 8, 9],[5,9,8]]])
print(f"arry d3: {arr3d},dimensoes: {arr3d.ndim}")

#shape
#omcoa p ta,emap dp arry
print(f"shape do arr1d: {arr1d.shape}")
print(f"shape do arr2d: {arr1d.shape}")
print(f"shape do arr3d: {arr1d.shape}")