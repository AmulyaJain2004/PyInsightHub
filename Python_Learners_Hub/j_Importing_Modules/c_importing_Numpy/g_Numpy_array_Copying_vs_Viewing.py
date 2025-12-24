#numpy array copy vs view

import numpy as np

original_array1 = np.array([1,2,3,4,5])

copied_array = original_array1.copy() #copies array or creates reference meaning manipulating copied array (independent array) will not change original array
copied_array[0] = 99
print("Copied array: ", copied_array)

array_view = original_array1.view() #copies array but manipulating copied array will change original array also.
array_view[0] = 99

print("Original array ", original_array1)
print("array view", array_view)

original_array = np.array([[1,2,3],[4,5,6]])
array_view = original_array.view()

array_view.shape = (3,2)
array_view[0][0] = 69

print("original array: ")
print(original_array)
print("Array view: ")
print(array_view)
