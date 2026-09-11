import pandas as pd

df = pd.read_csv("04-pokemon-data.csv", index_col = "Name")
# Filtering = keeping the rows that match a condition

# tall_pokemon = df[df["Height"] >= 2]

fire_pokemon = df[(df["Type1"] == "Fire") |
                  (df["Type2"] == "Fire")]

print(fire_pokemon)
