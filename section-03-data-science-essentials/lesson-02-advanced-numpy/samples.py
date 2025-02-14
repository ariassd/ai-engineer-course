import numpy as np

print("ARRAY AND SCALAR BROADCASTING")

arr = np.array([1, 2, 3])
print(arr + 10)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([1, 0, 1])
print(matrix + vector)

print("========\n")

print("AGGREGATION FUNCTIONS")

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Sum:", np.sum(arr))
print("Mean: ", np.mean(arr))
print("Max:", np.max(arr))
print("Min: ", np.min(arr))
print("Standard Deviation: ", np.std(arr))
print("Sum along rows: ", np.sum(arr, axis=1))
print("Sum along columns:", np.sum(arr, axis=0))

print("========\n")


print("BOOLEAN INDEXING AND FILTERING ")

arr = np.array([1, 2, 3, 4, 5, 6])
evens = arr[arr % 2 == 0]
print("Evens: ", evens)

arr[arr > 3] = 0
print("Modified Array: ", arr)
print("========\n")


print("RANDOM NUMBER GENERATION AND SETTING SEEDS")

random_array = np.random.rand(3, 3)
print("Random array\n", random_array)

random_integers = np.random.randint(0, 10, size=(2, 3))
print("Random Integers\n", random_integers)

print("Fix the output of random with a seed, this is useful for testing and training")
np.random.seed(42)

print("Random Integers SEED 42\n", np.random.randint(0, 10, size=(2, 3)))
print("Random Integers SEED EXPECTED\n", [[6, 3, 7], [4, 6, 9]])

print("========\n")
