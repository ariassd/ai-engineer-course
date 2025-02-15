# Hands-On Exercises
# • Exercise 1: Clean a Dataset by Handling Missing Values and Renaming
# Columns
# • Exercise 2: Merge Two Datasets and Perform Data Transformations
# • Additional Practice
#      • Drop columns with more than 50% missing values
#      • Merge three datasets and analyze relationships between them
#      • Convert categorical data to numerical using one-hot encoding


import pandas as pd
import numpy as np

df1 = pd.DataFrame(
    {"ID": [1, 2, 3], "Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
)
df2 = pd.DataFrame({"ID": [1, 2, 3], "Score": [85, 90, 88]})


print("dataset 1: \n", df1)
print("dataset 2: \n", df2)

merged = pd.merge(df1, df2, how="inner", on="ID")


print("Merged dataset: \n", merged)

merged["Score_Percentage"] = (merged["Score"] / 200) * 100

print("Transformed dataset: \n", merged)
