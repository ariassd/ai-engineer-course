import numpy as np


# Hands-On Exercises
# • Exercise 1: Create Vectors and Matrices Using NumPy
# • Exercise 2: Implement Matrix-Vector Multiplication
# • Exercise 3: Explore Special Matrices
# • Additional Practice
#   • Compute the determinant and inverse of a 2×2 matrix using NumPy
#   • Verify properties of matrix multiplication
#   • Create a block diagonal matrix using NumPy

# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[9, 48], [7, 6]])
# Addition
print("Addition\n", A + B)
# Subtraction
print("Subtraction\n", A - B)
# Scalar Multiplication
print("Scalar Mult: \n", 3 * A)


# Create matrix and vector
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = np.array([1, 0, -1])
# Matrix-vector multiplication
result = np.dot(M, v)
print("Matrix- Vector Multiplication: \n", result)


# Identity Matrix
I = np.eye(3)
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("A X I: \n", np.dot(A, I))

# Diagboal and Zero Matrix

D = np.diag([1, 7, 9])
Z = np.zeros((3, 3))

print("Diagonal Matrix\n", D)

print("Zero Matrix\n", Z)

print("=========ADDITIONAL PRACTICE: \n")
m1 = np.array([[1, 2], [3, 4]])

det = np.linalg.det(m1)

print("Determinant of the matrix is:", det)

# Calculate the determinant to check if the matrix is invertible
if det != 0:
    # Calculate the inverse of the matrix
    A_inv = np.linalg.inv(A)
    print("Inverse of the matrix is:")
    print(A_inv)
else:
    print("The matrix is singular and does not have an inverse.")
