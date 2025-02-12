# Exercise 1: Generate Arrays for Basic Mathematical Operations
# Exercise 2: Create a 3x3 Matrix and Perform Operations

import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Original matrix")
print(matrix)

print("TRANSPOSE")
transpose = matrix.T
print(transpose)


another_matrix = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Addition: \n", matrix + another_matrix)
print("Multiplication : \n", matrix * another_matrix)


print("ADDITIONAL PRACTICE")
four_four = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]).reshape(
    (4, 4)
)

print("Original matrix\n", four_four)
summary = {"col": {}, "row": {}}
for rowIx, array in enumerate(four_four, start=1):
    if f"row-{rowIx}" not in summary:
        summary["row"][f"row-{rowIx}"] = 0  # Initialize the key with 0

    for colIx, num in enumerate(array, start=1):
        # Adding row summary

        summary["row"][f"row-{rowIx}"] = summary["row"][f"row-{rowIx}"] + num
        # Adding col summary
        if f"col-{colIx}" not in summary:
            summary["col"][f"col-{colIx}"] = 0  # Initialize the key with 0
        summary["col"][f"col-{colIx}"] = summary["col"][f"col-{colIx}"] + num

print(summary["col"])
print(summary["row"])
