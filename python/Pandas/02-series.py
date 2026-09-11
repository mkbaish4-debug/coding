# series = A pandas 1-dimensional labled array that can hold any data type
# think of it like a  spreadsheet with a single column (1-dimensional)

# import pandas as pd

# marks = [34, 56, 78, 98, 65, 76]

# series = pd.Series(marks)

# print(series)


# or if we want custom labeling


# import pandas as pd

# marks = [34, 56, 78, 98, 65.7, 76]

# series = pd.Series(marks, index = ["Dhruv", "Peter", "Shahil", "Sidhanshu", "Shiva", "Mayank"])

# # print(series)
# # or
# print(series[series < 78])


#or you can directly insert a dictionary


import pandas as pd

marks = {"Dhruv": 34, "Peter": 56, "Shahil": 78, "Sidhanshu": 98, "Shiva": 65.7, "Mayank": 76}

series = pd.Series(marks)

# print(series)

# loc & iloc

series.loc["Shahil"] = 77 # or series.iloc[2] = 7

# iloc is used to access the location of labeling by integer

print(series.loc["Shahil"])
