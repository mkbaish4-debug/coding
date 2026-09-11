import pandas as pd

df = pd.read_csv("04-pokemon-data.csv", index_col = "Name")

pokemon = input("What is the name of your favourite pokemon?: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found!")


