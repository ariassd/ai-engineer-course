# Hands-On Exercises
# • Exercise 1: Load and Explore a Sample Dataset
# • Exercise 2: Select Specific Columns and Filter Rows
# Additional Practice
# • Load a local Excel file and explore its structure
# • Create a DataFrame from a dictionary and add a new calculated column
# • Save filtered data to a new CSV file


import pandas as pd
import requests
from io import StringIO

# f you need to bypass SSL verification (this is insecure and not recommended in production), you can use ssl to ignore certificate verification
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# Load Dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
response = requests.get(url)
data = StringIO(response.text)
df = pd.read_csv(data)

# Explore structure
print("First 5 rows: \n", df.head(5))
print("Last 5 rows: \n", df.tail(5))
print("Info: \n", df.info())
print("Describe: \n", df.describe())

print("======================\n")


print("SELECT COLUMNS")


selected_columns = df[["species", "sepal_length"]]
print("Selected columns: \n", selected_columns)

print("======================\n")

print("FILTER ROWS")
filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("Filtered rows: \n", filtered_rows)

print("======================\n")
