import numpy as np
arr1 = np.array([0,1,2,3,4])
print(arr1[2])
print(arr1[-1])

arr_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr_2d[1,2])
print(arr_2d[1][2])


arr = np.array([0,1,2,3,4,5,6,7,8,9])
mask = arr > 2
print(arr[mask])
