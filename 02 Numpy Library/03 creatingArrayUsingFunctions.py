import numpy as np

# creating zeros array
arr1 = np.zeros(4) # 1-D
arr2 = np.zeros((4,6)) # 2-D

# printing arrays
print(arr1)
print(arr2)

# creating ones array
arr3 = np.ones(5) # 1-D
arr4 = np.ones((5,2)) # 2-D

# printing arrays
print(arr3)
print(arr4)

# creating empty array
arr5 = np.empty(4) #1-D

# printing arrays
print(arr5)

# using arange function
arr6 = np.arange(4)

# printing array
print(arr6)

# Identity matrix
arr7 = np.eye(3)
arr8 = np.eye(3,5)

# printing array
print(arr7)
print(arr8)

# using linspace
arr9 = np.linspace(0,20,num=5)

# printing array
print(arr9)