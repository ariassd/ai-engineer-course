# Applying Data Manipulation and Visualization for EDA
# • What is EDA?
# • Steps in EDA
#    • Data Cleaning ✅
#    • Data Transformation ✅
#    • Aggregation and Filtering ✅

# Identifying Patterns, Trends, and Correlations
# • Visual Tools for Insights:
#     • Line plots for trends over time
#     • Bar charts for categorical comparisons
#     • Scatter plots for relationships
#     • Heatmaps for correlation analysis
# • Key Patterns to Look For:
#     • Relationships between variables (correlations)
#     • Distribution of variables (histograms, boxplots)
#     • Outliers or anomalies

# Hands-On Project: EDA on a Sample Dataset
# • Task 1: Perform Data Cleaning, Aggregation, and Filtering
# • Task 2: Generate Visualizations to Illustrate Key Insights
# • Task 3: Identify and Interpret Patterns or Anomalies
# • Task 4: Summarize Findings in a Report

# Additional Practice
# Use another dataset and apply the same EDA steps
# Explore advanced visualizations like boxplots or pairplots in Seaborn
# Create a dashboard for your findings using Plotly or Dash.


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests
from io import StringIO


print("===========================")


# Load Dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
response = requests.get(url)
data = StringIO(response.text)

df = pd.read_csv(data)

print(df.info())
print(df.describe())

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove duplicates
df = df.drop_duplicates()

# Filter data: Passengers in first class
first_class = df[df["Pclass"] == 1]
print("First Class Passengers: \n", first_class.head())


# Bar Chart: Survival rate by class
survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar", color="skyblue")
plt.title("Survival Rate by class")
plt.ylabel("Survival Rate")
plt.show()


# Histogram: Age distribution
sns.histplot(df["Age"], kde=True, bins=20, color="purple")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# Scatter Plot: Age vs Fare
plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="green")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()
