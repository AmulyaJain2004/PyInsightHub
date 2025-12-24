import numpy as np

array_1d = np.array([1,2,3,4,5])
array_2d = np.array([[1,2,3],[4,5,6]])
array_3d = np.array([[[1,2],[3,4],[5,6],[7,8]]])

print("Shape of 1d array:", array_1d.shape)
print("Shape of 2d array:", array_2d.shape)
print("Shape of 3d array:", array_3d.shape)

arr = np.array([1,2,3,4], ndmin=5)
print(arr)
print("Shape of array: ", arr.shape)
'''
arr = np.array([1,2,3,4], ndmin=5): This line creates a NumPy array with the values [1, 2, 3, 4] and sets the minimum number of dimensions of the array to 5 using the ndmin parameter. This means that even though the input is a 1-dimensional array, NumPy will create a multi-dimensional array with at least 5 dimensions. The shape of this array will depend on how NumPy chooses to reshape it to satisfy the condition of having at least 5 dimensions.
print(arr): This line prints the array arr. Since ndmin is set to 5, the printed array might look complex and might not be easy to interpret visually.
print("Shape of array: ", arr.shape): This line prints the shape of the array arr. The shape of an array is a tuple of integers indicating the size of the array in each dimension. It provides information about the number of elements along each axis/dimension of the array.
'''

'''
The output of print(arr) will show the actual array that NumPy creates. Since ndmin is set to 5, the array will have at least 5 dimensions, but the exact shape may vary depending on how NumPy reshapes it. This output might be complex and difficult to interpret directly without knowing the internal reshaping rules of NumPy.
The output of print("Shape of array: ", arr.shape) will show the shape of the array. This will give us insight into how NumPy reshaped the input array to meet the condition of having at least 5 dimensions. It will be a tuple of integers representing the size of the array along each dimension.
'''
