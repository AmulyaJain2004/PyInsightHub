import numpy as np

original_array = np.array([1,2,3,4,5,6])

reshaped_array = original_array.reshape(2,3)

print("Original array: ")
print(original_array)

print("Reshaped array: ")
print(reshaped_array)

row_major = original_array.reshape(2,3, order='C')
column_major = original_array.reshape(2,3, order='F')

print("Original array: ")
print(original_array)

print("Row-major reshaped array: ")
print(row_major)
print("Column-major reshaped array: ")
print(column_major)
