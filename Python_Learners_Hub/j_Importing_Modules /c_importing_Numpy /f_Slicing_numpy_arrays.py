import numpy as np

arr = np.array([0,1,2,3,4,5,6,7,8,9])
slice_result  = arr[2:6]
print(slice_result)

arr_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
slice_result  = arr_2d[0:2, 1:3]
print(slice_result)

arr = np.array([0,1,2,3,4,5,6,7,8,9])
slice_result  = arr[1:9:2]
print(slice_result)
