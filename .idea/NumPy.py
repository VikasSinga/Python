import numpy as np

# 1-d array
arr = np.array([1,2,3,4,5,6])
print(arr[1])
print(type(arr))
print(np.__version__)

# Indexing 1 example
print(arr[1]+arr[3]+arr[2])

# 2d array

arr1 = np.array([[3,4,5,6,7],[2,4,6,8,9]])
print(arr1[0][3])

# 3-d array

arr2 = np.array([[[1,2,3],[2,3,4]],[[4,5,6],[5,6,7]]])
print(arr2[1][0][0])

arr3=np.array([6,7,8,9],ndmin=10)
print(arr3)

# Arr Slicing
arr4= np.array([1,2,3,4,5,6])
print(arr4[1:4])
print(arr4[1:])
print(arr4[:5])