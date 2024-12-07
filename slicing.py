#======= slicing========
import numpy as np
array_2D=np.array([[1,2,3],[4,5,6],[7,8,9]],int)
print(array_2D)
print(array_2D[:,1])
print(array_2D[0,:])
print(array_2D[0:2,0:2])
print(array_2D.shape)
# reshape=array_2D.reshape(1,9)
# print(reshape)

row_len=(len(array_2D))-1
col_len=(len(array_2D[0]))-1
Sum=(array_2D[0,0]+array_2D[row_len,col_len])
print(Sum)