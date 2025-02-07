numbers = [1, 2, 3, 4]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "apple", True]
# print (numbers [2])
# print(fruits[-1])
# print(mixed [1])
fruits.append("orange")
fruits.insert(1, "grape")

print(fruits)
fruits.remove("banana")
print(fruits)
del fruits[0]
print(fruits)
fruits.pop()
fruits.pop()
print(fruits)


sliced_fruits = fruits[1:4]
print(sliced_fruits)
