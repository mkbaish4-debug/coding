import numpy as np


# Filtering = It refers to the data where only the
#  selected elements are represented out of an array
# following a certain condition

ages = np.array([[12, 45, 65, 34, 23, 13, 18],
                 [19, 54, 25, 27, 98, 76, 65]])

# adults = ages[(ages >= 18) & (ages < 65)]
# teenagers = ages[(ages > 12) & (ages < 18)]
# seniors = ages[ages >= 65]

# print(adults)
# print(teenagers)
# print(seniors)

# If we want to preserve the shape then,

adults = np.where((ages>=18) & (ages<65), ages, 0)

print(adults)
