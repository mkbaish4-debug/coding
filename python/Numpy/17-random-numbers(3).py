import numpy as np

rng = np.random.default_rng()

# shuffle function

# array = np.array([1, 2, 3])

# rng.shuffle(array)
# print(array)

# choice function

fruits  = np.array(["🍎", "🍌", "🥭", "🥥"])

fruits = rng.choice(fruits, size = (3, 3))
print(fruits)
