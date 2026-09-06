import numpy as np

array = np.array([[[1, 2, 4], [2, 3, 4], [2, 3, 4]],
                 [[3, 5, 6], [2, 3, 7], [2, 3, 4]]])

# print(array[1][0][0]) chain indexing
print(array[1, 0, 1]) # multidimensional indexing
# print(array[1, 0][0]) # mixed indexing

