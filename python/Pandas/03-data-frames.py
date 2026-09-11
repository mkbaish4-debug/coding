# DataFrames = It is a data stucture in a tabular form like a 2-D spreadsheet

import pandas as pd

data = {"Name": ["Mayank", "Sidahnshu", "Shahil", "Shiva"],
      "Age": [19, 22, 19, 20]
}

df = pd.DataFrame(data, index = ["Student 1", "Student 2", "Student 3", "Student 4"]) # custom labeling can be done

# print(df)

# Add a column
df["Marks"] = [76, 87, 65, 88]

# print(df)

# Add rows
new_rows = pd.DataFrame([{"Name": "Vimal",
                        "Age": 19,
                        "Marks": 70},
                        {"Name": "Abhishek",
                         "Age": 21,
                         "Marks": 61}],
                        index = ["Student 5", "Student 6"])

df = pd.concat([df, new_rows])

print(df)
