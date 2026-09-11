import pandas as pd

df = pd.read_csv("04-pokemon-data.csv")

# Aggregation = reduces a set of values into a single value
#               Used to analyze and summarise the data
#               Often used with the groupby() function


# Used for the whole dataframe
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# for Single column
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Type2"].count())

group = df.groupby("Type1")

# print(group["Height"].mean())
print(group["Height"].count())
