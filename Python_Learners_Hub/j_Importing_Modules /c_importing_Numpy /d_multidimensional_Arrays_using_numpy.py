import numpy as np

arr_1d = np.array([1,2,3,4,5])
print(arr_1d)

arr_2d = np.array([[1,2,3], [4,5,6]])
print(arr_2d)

arr_3d = np.array([[[1,2,3],[4,5,6],[1,2,3],[4,5,6]]])
print(arr_3d)

arr = np.array([1,2,3,4,5], ndmin=5) #ndmin is for mininum number of dimensions
print(arr)
print('Number of dimensions :', arr.ndim)
