# Combining and Merging DataFrames
# • Concatenation
# • Merging
# • Joining


import pandas as pd


print("CONCATENATION RENAME\n")

# Load Dataset
fileName = "./ds1.xlsx"

df1 = pd.read_excel(fileName)
print("XC File\n", df1)

df2 = pd.read_excel(fileName)
# print("XC File\n", df2)

df3 = pd.concat([df1, df2], axis=0)
print("concat axis 0\n", df3)

df3 = pd.concat([df1, df2], axis=1)
print("concat axis 1\n", df3)

bets = pd.read_excel("ds2.xlsx")

# This is like a inner join between two tables of SQL
merged = pd.merge(df1, bets, on="gid")
print("merge DEFAULT (INNER)\n", merged)

# This is like a LEFT Join
merged = pd.merge(df1, bets, how="left", on="gid")
print("merge LEFT\n", merged)

# This is like a LEFT Join
merged = pd.merge(df1, bets, how="inner", on="gid")
print("merge INNER\n", merged)


print("======================\n")

df1 = pd.read_excel("ds1.xlsx")
bets = pd.read_excel("ds2.xlsx")

df1 = df1.dropna()
df1 = df1.dropna(axis=1)

# This is like a LEFT Join
joined = df1.join(bets, how="left", on=["gid"], lsuffix="_left", rsuffix="_right")
print("JOINED INNER\n", joined)
