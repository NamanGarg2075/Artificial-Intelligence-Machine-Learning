import numpy as np

# All these functions are under random module
# rand() - generate number between 0 and 1 only
# randn() - generate number close to zero can be positive or negative
# randf() - generate numbers betwen [0.0, 1.0)
# randint() - generate number between given range

# rand()
arr1 = np.random.rand(5) # 1-D
arr2 = np.random.rand(4,5) # 2-D

print(arr1)
print(arr2)

# randn()
arr3 = np.random.randn(2) # 1-D
arr4 = np.random.randn(3,4) # 2-D

print(arr3)
print(arr4)

# randf()
arr5 = np.random.ranf(4) # 1-D
arr6 = np.random.ranf((3,4)) # 2-D

print(arr5)
print(arr6)

# randint(min,max,total_values)
arr7 = np.random.randint(3,10,100)

print(arr7)