# import numpy as np
# array=np.array([1,2,3,4,5,6,7,8,9,10],int)
# print(array)
# array_2D=np.array([[1,2,3],[4,5,6],[7,8,9]],int)
# print(array_2D)
# array_3D=np.array([[[1,2,3],[4,5,6],[7,8,9]]],int)
# print(array_3D)
# print(array_3D.ndim)
# Sum=0
# for i in range(0,len(array)):
#     Sum=Sum+array[i]
# print(Sum)
# print(array_2D[0,0])
from random import random

# x=0
# for i in range(1,11):
#     x=x+i
# print(x)
# y=0
# for i in range(1,5):
#     for j in range(1,2):
#         y=y+j
# print(y)

# row=6
# for i in range(1,row+1):
#     i =row*i
#     print("i"*i)

# print("arman"*2)
row=5
for i in range(1,row+1):
    print(" "*(row-i)+("*"*(2*i-1)))

rows = 5  # Number of rows
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
