# Aggregation Functions
# • Using groupby
# • Using pivot_table
# • Custom Aggregation
# • Apply custom functions using .agg()

import pandas as pd


print("ADDITIONAL PRACTICE\n")

# Load Dataset
fileName = "data.csv"
df = pd.read_csv(fileName, sep=";")

print("CSV File\n", df)

print("======================\n")

print("GROUP PRACTICE\n")

grouped = df.groupby("contributorType")

for name, group in grouped:
    print(name)
    print(group)

print("======================\n")

print("AGGREGATIONS PRACTICE\n")

print("MEAN\n", grouped.mean("xpContributionPercentage"))
print("SUM\n", grouped.sum("xpContributionPercentage"))

print("======================\n")

mean = df.groupby("contributorType")["xpContributionPercentage"].mean()
print("MEAN\n", mean)

aggregation_combine = (
    df.groupby("contributorType")
    .agg({"xpContributionPercentage": ["mean", "max", "min"]})
    .mean()
)

print("AGGREGATION_COMBINE\n", aggregation_combine)

print("======================\n")

print("PIVOT TABLE\n")

pivot = df.pivot_table(
    values="xpContributionPercentage", index="contributorType", aggfunc="mean"
)

print("PIVOT\n", pivot)

print("======================\n")


print("CUSTOM AGGREGATION\n")


def range_function(x):
    return x.max() - x.min()


custom_agg = mean = df.groupby("contributorType")["xpContributionPercentage"].agg(
    range_function
)

print("CUSTOM_AGG\n", custom_agg)

print("======================\n")
