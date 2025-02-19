import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013]
sales = [100, 120, 140, 160]

plt.plot(years, sales, label="Sales trend", color="blue", marker="o")
plt.title("Sales over years")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend()
plt.show()

# Bar chart
categories = ["electronics", "Clothing", "Groceries"]
revenue = [250, 400, 150]
plt.bar(categories, revenue, color="green")
plt.title("Revenue by category")
plt.show()
