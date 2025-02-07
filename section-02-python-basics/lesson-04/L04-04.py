numbers = {1, 2, 3, 4}
empty_set = set()
print(numbers)
numbers.add(8)
print(numbers)
numbers.remove(2)
print(numbers)


set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("union", set1 | set2)
print("intersection", set1 & set2)
print("diff", set1 - set2)
