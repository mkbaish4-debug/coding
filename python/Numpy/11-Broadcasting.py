import numpy as np

# broadcasting allows numpy to perform operations on arrays
# of diff shapes by virtually expanding the dimensions of the arrays
# such that they match the larger array's shape

# the condition are that either The dimensions are equal,
# or
# One of the dimensions is 1.

array1 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])


array2 = np.array([[1], [2], [3]])

print(array1.shape)
print(array2.shape)

print(array1*array2)
