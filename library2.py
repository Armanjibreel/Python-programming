# import numpy as np
# array1=np.array([1,2,3,4,5])
# array2=np.array([6,7,8,9,10])
# array3=np.concatenate((array1,array2))
# print(array3)
from enum import unique

# import numpy  as np
# arr=np.array([1,2,3,4,5,6,7,8,9])
# split=np.array_split(arr,3)
# print(split)

#----------ravel and flater-----
# convert multidimensional array into 1d array

# import numpy as np
# arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr1)
# print(arr1.ndim)
# ravel=arr1.ravel()
# ravel[0]=99
# print(ravel)
# print(ravel.ndim)
#
# import numpy as np
# arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr1)
# print(arr1.ndim)
# flatten=arr1.flatten()
# flatten[0]=99
#
# print(flatten)
# print(flatten.ndim)
#
# import numpy as np
# arr1=np.array([1,2,3,2,3,4,5,6,5,7])
# print(arr1)
# arr2=np.unique(arr1,return_index=True)
# print(arr2)
#
# import numpy as np
# arr1=np.array([1,2,3,2,3,4,5,6,5,7])
# print(arr1)
# arr2=np.unique(arr1,return_counts=True)
# print(arr2)
# import numpy as np
# arr_2D=np.array([[2,2,3],[4,4,6],[9,8,9]])
# arr1_2D=np.unique(arr_2D)
# print(arr1_2D)

import numpy as np
arr=np.zeros((2,3))
print(arr)
arr1=np.ones((2,3))
print(arr1)
arr2=np.eye(3)
print(arr2)
arr3=np.linspace(3,3,3)
print(arr3)