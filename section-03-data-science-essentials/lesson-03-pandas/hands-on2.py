# Hands-On Exercises
# • Exercise 1: Load and Explore a Sample Dataset
# • Exercise 2: Select Specific Columns and Filter Rows
# Additional Practice
# • Load a local Excel file and explore its structure
# • Create a DataFrame from a dictionary and add a new calculated column
# • Save filtered data to a new CSV file


import pandas as pd


print("ADDITIONAL PRACTICE\n")

# Load Dataset
fileName = "./ds1.xlsx"
df = pd.read_excel(fileName)

print("XC File\n", df)

print("======================\n")

print("FILTER ROWS")

filtered_rows = df[(df["contribution"] >= 1)]

print(filtered_rows)

print("======================\n")


print("ADDING TYPE TO FIRST 5 AND SPORTS TO THE REST")

df["type"] = "sports"
df.iloc[:7, df.columns.get_loc("type")] = "casino"

print(df)

print("======================\n")

print("EXPORT DATA")

df.to_csv(fileName + "-export.csv", sep=";")

print("======================\n")
