import numpy as np

# creating arrays
arr1 = np.array([1,2,3]) # 1-D
arr2 = np.array([[1,2,3],[4,5,6]]) # 2-D
arr3 = np.array([[[1,2,3],[4,5,6]],
                 [[1,2,3],[4,5,6]]]) # 3-D

# finding dimentions
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# creating multidimentional array
arr4 = np.array([1,2,3,4],ndmin = 10) # 10-D
print(arr4)
print(arr4.ndim)