import matplotlib.pyplot as plt


print("BASIC PLOT")
# Basic Plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.show()

print("===========================")


print("X-Y AXIS AND TITLE BASIC PLOT")

# Line Plot
plt.plot([1, 2, 3], [10, 20, 30], label="Trend")
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

print("===========================")

print("BAR CHART")

categories = ["A", "B", "C"]
values = [10, 20, 7]
plt.bar(categories, values, color="blue")
plt.title("Bar Chart")
plt.show()

print("===========================")

print("HISTOGRAM")

data = [1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4]

plt.hist(data, bins=4, color="green", edgecolor="black")
plt.title("Histogram")
plt.show()

print("===========================")

print("SCATTER PLOT")

x = [1, 2, 3, 4, 5]
y = [10, 12, 25, 30, 45]

plt.scatter(x, y, color="red")
plt.title("Scatter")
plt.show()

print("===========================")
