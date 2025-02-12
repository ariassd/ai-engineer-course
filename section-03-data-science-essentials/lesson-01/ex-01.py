import numpy as np

print("\nNP ARRAY")
arr = np.array([1, 2, 3, 4])
print(arr)


print("\nNP ZERO ARRAY")
zeros = np.zeros((3, 3))
print(zeros)

print("\nNP ONES ARRAY")
ones = np.ones((2, 4))
print(ones)

print("\nCount from 0 to 10 interval of 3")
# Count from 0 to 10 interval of 3
range_array = np.arange(0, 10, 3)
print(range_array)

print("\nCount from 0 to 10 interval of 2")
# Count from 0 to 10 interval of 2
range_array = np.arange(0, 10, 2)
print(range_array)


print("\nLinspace function")
# (0, 10, 5) => [ 0.   2.5  5.   7.5 10. ]
# (0, 10, 6) => [ 0.  2.  4.  6.  8. 10.]
# (1, 10, 3) => [ 1.   5.5 10. ]
linspace_array = np.linspace(1, 10, 5)
print(linspace_array)

print("\nReshaping arrays")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Original array", arr)
reshaped = arr.reshape((3, 3))
print("Reshaped array", reshaped)


print("\nAdding dimentions")
arr = np.array([1, 2, 3, 4, 5, 6])
print("Original array", arr)
expanded = arr[:, np.newaxis]
print(expanded)

print("\nArray operations")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Sum arrays")
print(a + b)
print("Multiply arrays")
print(a * b)
print("divide arrays")
print(a / b)

print("\nArray square")
arr = np.array([4, 16, 25])
print("SQR", np.sqrt(arr))
print("SUM", np.sum(arr))
print("The mean is the average of the numbers (4+16+25)/3 = ", np.mean(arr))
print("MAX", np.max(arr))


print("SUB ARRAYS WITH NUMPY")
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[2])
print(arr[-1])
print(arr[1:4])
print(arr[3:])
reshaped = arr.reshape(2, 3)
print(reshaped)
