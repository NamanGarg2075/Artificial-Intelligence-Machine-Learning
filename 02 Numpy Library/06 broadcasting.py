import numpy as np

# creating arrays
arr1 = np.array([1,2,3,4])
arr2 = np.array([1,2,3])

# print(np.add(arr1,arr2)) # broadcasting error

# rules
# dimention same or
# last element same or
# atleast one of two dimentions' last element is 1

# then broadcast error will resolved