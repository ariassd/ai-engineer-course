# Loop in list
fruits = ["apple", "banana", "cherry"]
for item in fruits:
    print(item)


# Loop in range
for i in range(5):
    print(i)

# While Loop
count = 5
while count > 0:
    print(count)
    count -= 1


# Break
for i in range(10):
    if i == 5:
        break
    print(i)


# Continue
for i in range(10):
    if i == 5:
        continue
    print(i)

# Continue
for i in range(10):
    if i % 2:
        continue
    print(i)

# 1
# 3
# 5
# 7
# 9
