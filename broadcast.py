from imports import *

array = np.eye(3)

print(array[1])

array[1][0] = 0
array[1][1] = 0
array[1][2] = 0

array[1] = [0,0,0]

print(array[1])