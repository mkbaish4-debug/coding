import pandas as pd

df = pd.read_csv("04-pokemon-data.csv", index_col = "Name") # we can change the labeling from 0-n to a column

# # selection by column
# print(df[["Name", "Height", "Weight"]].to_string())

# selection by row
print(df.loc["Charizard":"Pikachu":2, "Height":"Legendary":2])
# we can apply all the slicing, indexing concepts

# alternatively
# print(df.iloc[0:11:3, 0:4:2])

