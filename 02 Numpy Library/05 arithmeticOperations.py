import numpy as np

# creating arrays
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

# adding scalar (+/-)
print(arr1 +3)

# adding array 
print(arr1 + arr2)

# dividing array
print(arr1/arr2)

# modulus
print(arr2%arr1)

# power
print(arr1**arr2)

# reciprocal
print(np.reciprocal(arr1))