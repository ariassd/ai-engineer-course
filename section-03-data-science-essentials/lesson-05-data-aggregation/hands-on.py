# HANDS ON

# Hands-On Exercises
# • Exercise 1: Group Data by a Categorical Column
# • Exercise 2: Calculate Summary Statistics for Grouped Data


# • Additional Practice
#      • Create a dataset of sales data and group it by region or product category
#      • Use pivot_table to calculate total sales per region and per year
#      • Create a custom aggregation function to calculate the variance for each group

import pandas as pd

data = {
    "Class": ["А", "в", "А", "в", "С", "С"],
    "Score": [85, 90, 88, 72, 95, 80],
    "Age": [15, 16, 15, 17, 16, 15],
}
df = pd.DataFrame(data)
print("Original Dataset yn", df)
grouped = df.groupby("Class").mean()
print(grouped)


stats = df.groupby("Class").agg(
    {
        "Score": ["mean", "max", "min"],
        "Age": ["mean", "max", "min"],
    }
)

print("STATS", stats)
