# Hands-On Exercises
# • Exercise 1: Clean a Dataset by Handling Missing Values and Renaming
# Columns
# • Exercise 2: Merge Two Datasets and Perform Data Transformations

import pandas as pd
import numpy as np

# Create a sample dataset
data = {
    "Name": ["Alice", "Bob", np.nan, "David"],
    "Age": [25, np.nan, 30, 35],
    "Score": [85, 90, np.nan, 88],
}


df = pd.DataFrame(data)
print("Original Dataset: \n", df)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()
print("Dataset: \n", df)
df = df.rename(columns={"Name": "Student_Name", "Score": "Exam: Score"})

print("Dataset: \n", df)
