import pandas as pd

print("DATA FRAME")
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)
data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
print(df)
print("======================\n")

print("SAVE DATA FROM EXCEL")
data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)
# df.to_excel("data.xlsx", index=False)

print("======================\n")

# print("LOAD DATA FROM EXCEL")
# df = pd.read_csv("data.csv")
# df = pd.read_excel("data.xlsx")

# print("======================\n")


print("VIEW DATA")
data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)

print("Head", df.head())
print("Head", df.tail(3))
print("INFO", df.info())
print("DESCRIBE", df.describe())

print("======================\n")

print("SELECT AND INDEX")
print("COLUMN1\n", df[["Name"]])
print("COLUMN2\n", df[["Age"]])
print("COLUMN1-2\n", df[["Name", "Age"]])


print("======================\n")

print("FILTER ROWS")
print("FILTER Age > 25\n", df[df["Age"] > 25])


print("======================\n")

print("SELECT BY POSITION")
print("FIRST ROW\n", df.iloc[0])
print("FIRST COL\n", df.iloc[:, 0])


print("======================\n")


print("SELECT BY LABEL")
print("FIRST ROW\n", df.iloc[0])
print("FIRST COL\n", df.iloc[:, "Name"])


print("======================\n")
