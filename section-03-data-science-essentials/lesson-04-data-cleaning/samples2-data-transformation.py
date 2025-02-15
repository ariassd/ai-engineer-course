# Data Transformations
# • Renaming Columns
# • Changing Data Types
# • Creating or Modifying Columns

import pandas as pd


print("COLUMN RENAME\n")

# Load Dataset
fileName = "./ds1.xlsx"

df = pd.read_excel(fileName)
print("XC File\n", df)

df = df.rename(columns={"contribution": "percentage"})

print("XC Fixed file\n", df)

print("======================\n")

print("TYPE TRANSFORM\n")

df["percentage"] = df["percentage"].astype(dtype="float")
df["date"] = pd.to_datetime(df["date"])

print("XC Fixed file\n", df)

print("======================\n")

print("MODIFYING DATA\n")

df["new_col"] = df["percentage"] * 2

print("XC Fixed file\n", df)

print("======================\n")
