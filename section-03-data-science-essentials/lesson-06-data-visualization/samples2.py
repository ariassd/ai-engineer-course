import matplotlib.pyplot as plt


print("SCATTER PLOT")

x = [1, 2, 3, 4, 5]
y = [10, 12, 25, 30, 45]

plt.scatter(x, y, color="red")
plt.title("Scatter")
plt.xlabel("X axis label")
plt.ylabel("Y axis label")
plt.legend("Dataset")
plt.show()

print("===========================")

print("LINE BASIC PLOT")

# Line Plot
plt.plot(
    [1, 2, 3], [10, 20, 30], label="Trend", color="orange", linestyle="--", marker="p"
)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

print("===========================")
