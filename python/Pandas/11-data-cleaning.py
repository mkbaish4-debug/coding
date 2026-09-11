import pandas as pd

df = pd.read_csv("04-pokemon-data.csv")

# Data Cleaning = The process of fixing/removing/Modifying:
#                 incomplete, irrelevant, incorrect data
#                 ~75% of work done with pandas is data cleaning

# 1. Drop irrelevant columns
# df = df.drop(columns = ["Legendary", "No"])

# 2. Handle missing data
# df = df.dropna(subset = ["Type2"])
# df = df.fillna({"Type2": "None"})

# 3. Fix inconsistent values
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                   "Fire": "FIRE",
#                                   "Water": "WATER"})

# 4. Standardise text
# df["Name"] = df["Name"].str.lower()

# 5. Fix data types
# df["Legendary"] = df["Legendary"].astype(bool)

# 6. Remove duplicate values
# df = df.drop_duplicates()

print(df.to_string())
