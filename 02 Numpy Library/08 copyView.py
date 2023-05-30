import numpy as np

# copy()
#         Creats new array
#         Changes in original array does not refect in copy array
# view()
#         Creates copy of original array
#         Changes in original array reflects in view array and vice versa

# creating array
arr1 = np.array([1,2,3,4,5])

# creating copy of array
arr2 = arr1.copy()

# changes
arr1[1] = 100


# creating view of array
arr3 = arr1.view()

# changing
arr1[1] = 500

# printing array
print(arr1)
print(arr2)
print(arr3)