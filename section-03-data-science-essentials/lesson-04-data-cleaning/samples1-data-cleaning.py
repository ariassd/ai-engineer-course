# Handling Missing Values
# • Why Handle Missing Values?
# • Methods to Handle Missing Values
# • Drop Missing Values
# • Fill Missing Values
# • Interpolation


import pandas as pd


print("DATA CLEANING\n")

# Load Dataset
fileName = "./ds1.xlsx"

df = pd.read_excel(fileName)


print("XC File\n", df)

print("======================\n")

print("DROP NA\n")
df = df.dropna()
df = df.dropna(axis=1)
print("XC File\n", df)

print("======================\n")

print("FILL MISSING INFORMATION\n")
df = pd.read_excel(fileName)
print("XC File\n", df)


# DataFrame.fillna with 'method' is deprecated
# df["contribution"] = df["contribution"].fillna(0)
df = df.ffill()
df = df.bfill()
# df["contribution"] = df["contribution"].fillna(method="bfill")
print("XC Fixed File\n", df)


print("======================\n")

print("INTERPOLATION\n")
df = pd.read_excel(fileName)
print("XC File\n", df)


# Interpolation is the straight line between two points
df["contribution"] = df["contribution"].interpolate()

print("XC Fixed File\n", df)


print("======================\n")
