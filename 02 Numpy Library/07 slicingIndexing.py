import numpy as np

arr = np.array([1,2,3,4,5])

print(arr[1]) # 2
print(arr[1:5]) # 2 3 4 5
print(arr[::2]) # 1 3 5
print(arr[::-1]) # reverse array
print(arr[3::-1]) # 4 3 2 1