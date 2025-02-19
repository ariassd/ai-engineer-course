# Hands-On Exercises
# • Exercise 1: Create Basic Plots with Matplotlib
# • Exercise 2: Create a Heatmap with Seaborn
# • Additional Practice
#    • Create a histogram with multiple datasets overlaid
#    • Use Seaborn to create a violin plot or box plot for visualizing distributions
#    • Combine multiple plots in a single figure using Matplotlib's subplot


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests
from io import StringIO


print("VIOLIN")
# Example dataset: tips dataset
data = {
    "total_bill": [16.99, 10.34, 21.01, 23.68, 24.59],
    "tip": [1.01, 1.66, 3.50, 3.31, 3.61],
    "sex": ["Female", "Male", "Male", "Male", "Female"],
    "smoker": ["No", "No", "No", "No", "No"],
    "day": ["Sun", "Sun", "Sun", "Sun", "Sun"],
    "time": ["Dinner", "Dinner", "Dinner", "Dinner", "Dinner"],
    "size": [2, 3, 3, 2, 4],
}
custom_tips = pd.DataFrame(data)

# Create a violin plot for the total bill by day
plt.figure(figsize=(8, 6))
sns.violinplot(x="day", y="total_bill", data=custom_tips, palette="muted")

# Title and labels
plt.title("Violin Plot - Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")

# Show plot
plt.show()

print("===========================")


print("COMBINE PLOTS")

# Load a dataset
tips = custom_tips

# Create a figure and a set of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))  # 2 rows, 2 columns

# First subplot: Histogram of total bill
axes[0, 0].hist(tips["total_bill"], bins=10, color="green", edgecolor="black")
axes[0, 0].set_title("Histogram of Total Bill")
axes[0, 0].set_xlabel("Total Bill")
axes[0, 0].set_ylabel("Frequency")

# Second subplot: Boxplot of total bill by gender
sns.boxplot(x="sex", y="total_bill", data=tips, ax=axes[0, 1], palette="Set2")
axes[0, 1].set_title("Boxplot of Total Bill by Gender")

# Third subplot: Scatter plot of total bill vs tip
axes[1, 0].scatter(tips["total_bill"], tips["tip"], color="blue")
axes[1, 0].set_title("Total Bill vs Tip (Scatter)")
axes[1, 0].set_xlabel("Total Bill")
axes[1, 0].set_ylabel("Tip")

# Fourth subplot: Violin plot of total bill by day
sns.violinplot(x="day", y="total_bill", data=tips, ax=axes[1, 1], palette="muted")
axes[1, 1].set_title("Violin Plot of Total Bill by Day")

# Adjust the layout to prevent overlapping
plt.tight_layout()

# Show the combined plot
plt.show()
print("===========================")


print("HISTOGRAM")

# Sample datasets
data1 = [1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4]
data2 = [1, 1, 2, 3, 4, 4, 5, 5, 6, 6]

# Plotting the first dataset (green)
plt.hist(data1, bins=4, color="green", edgecolor="black", alpha=0.5, label="Dataset 1")

# Plotting the second dataset (blue)
plt.hist(data2, bins=4, color="blue", edgecolor="black", alpha=0.5, label="Dataset 2")

# Add titles and labels
plt.title("Histogram with Multiple Datasets")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Display the legend
plt.legend()

# Show the plot
plt.show()

print("===========================")


# Load Dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
response = requests.get(url)
data = StringIO(response.text)

df = pd.read_csv(data)
del df["species"]

# Calculate correlation matrix
correlation_matrix = df.corr()
# plot heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
