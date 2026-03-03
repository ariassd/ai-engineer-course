# Hands-On Exercises
# • Exercise 1: Calculate Determinant and Inverse of a Matrix
# • Exercise 2: Compute Eigenvalues and Eigenvectors
# • Exercise 3: Perform Singular Value Decomposition
# • Additional Practice
#     • Compute eigenvalues and eigenvectors for larger matrices
#     • Use SVD to reduce the dimensionality of a dataset
#     • Verify the property of eigenvalues: det (A - A1) = 0

import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


det = np.linalg.det(A)

inverse = np.linalg.inv(A)

print("det\n", det)
print("inv", inverse)


eigvalues, eigvectors = np.linalg.eig(A)

print("E Values", eigvalues)
print("E Vectors", eigvectors)


print("============ reconstructed")

A = np.array([[3, 1, 1], [-1, 3, 1], [1, 1, 3]])

U, S, Vt = np.linalg.svd(A)
print("U: \n", U)
print("Singular Values: \n", S)
print("V Transpose: \n", Vt)

# Reconstruct
sigma = np.zeros((3, 3))
np.fill_diagonal(sigma, S)
reconstructed = U @ sigma @ Vt


# •	@ operator: This operator performs matrix multiplication between two matrices (or arrays) when they are both NumPy arrays.
# •	np.dot(A, B): An alternative to @, which also performs matrix multiplication.


print("Reconstructed", reconstructed)
