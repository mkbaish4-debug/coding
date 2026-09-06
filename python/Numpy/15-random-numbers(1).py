import numpy as np

rng = np.random.default_rng(seed = 1)

# print(rng.integers(1, 7))
print(rng.integers(1, 7, size = (3, 2)))

# You can also use seed as to fixate&specify a particular random set
