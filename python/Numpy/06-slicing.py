import numpy as np

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                 [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                 [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])

# simple slicing
# print(array[start:end:step])
# print(array[::-1])

print(array[0:2,0,0:2]) #mix concept

