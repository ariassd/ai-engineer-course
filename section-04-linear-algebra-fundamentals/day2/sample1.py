# Determinants and Inverse of a Matrix
# • Determinants
# • Scalar value that provides information about a matrix's properties
# • Only for square matrices
# • det(A) = 0, the matrix A is singular
# • det(A)!= 0, A is invertible
# • Geometric Interpretation
#     • For a 2×2 matrix, the determinant represents the scaling factor of the are formed by its column vectors
#     • Formula for 2 × 2 Matrix:
#           det[[a,b]
#               [c,d]]  = ad - bc


import numpy as np

A = np.array([[2, 3], [1, 4]])


det = np.linalg.det(A)
print("Determinant: ", det)


# Determinants and Inverse of a Matrix
# • Inverse of a Matrix
# • denoted as A-1
# • Product of a matrix and its inverse is the identity matrix: A x A-1=1
# • Matrix is invertible only if det (A) != 0
# • Formula for 2 × 22×2 Matrix
#     a^-1 = (1/det(A))*[[d,-b],[-c,a]]


inverse = np.linalg.inv(A)
print("Inverse \n", inverse)


# Eigenvalues and Eigenvectors
# • What are Eigenvalues and Eigenvectors?
# • If A •0=2•v, then
#     • v is an eigenvector
#     • A is the eigenvalue
# • Geometric Interpretation
#     • Eigenvectors point in the direction where the matrix transformation stretches or compresses vectors
#     • Eigenvalues indicate the factor of stretching or compression
# • Properties
#     • Matrix of size n × n has n n eigenvalues and eigenvectors
#     • Eigenvalues can be real or complex
#     • For a symmetric matrix, eigenvalues are always real.
# • Computing Eigenvalues and Eigenvectors in NumPy

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigen values: \n", eigenvalues)
print("Eigen vectors: \n", eigenvectors)


B = np.array([[4, 1], [1, 1]])

print(np.linalg.eig(B))
