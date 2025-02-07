# List comprehensions

from functools import reduce

# Syntax
# [expression for item in iterable if condition]

# Create a list of squares
squares = [x**2 for x in range(10)]
print(f"Squares list is {squares}")


# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers list is {evens}")

# Lambda functions
# Syntax
# lambda arguments: expression

add = lambda x, y: x + y
print("Lamnda result ", add(3, 5))

# Map, filter and reduce

numbers = [1, 2, 3, 4]
squares = map(lambda x: x**2, numbers)
print("squares of map", list(squares))


filtered = filter(lambda x: x % 2 == 0, numbers)
print("filtered numbers ", list(filtered))


reverse = [numbers[(i + 1) * -1] for i in range(len(numbers))]
print("reversed", list(reverse))

#
#                     Accumulator       list
#                         ↓             ↓
#                |----------------| |------|
product = reduce(lambda x, y: x * y, numbers)
print("reduce product", product)
