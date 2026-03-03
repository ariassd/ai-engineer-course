# Matrix Operations


import numpy as np

print("=====================================")
# • Addition and Subtraction
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Addition: \n", A + B)
print("Subtraction: \n", A - B)


print("=====================================")
# • Scalar Multiplication
C = 2 * A
print("Scalar multiplication\n", C)


print("=====================================")
# • Matrix Multiplication -> It requires the number of columns of matrix A to be the same of number of rows of matrix B
#       Formula: (A • B)ij = ∑ k Aik Bkj
#       C_ij = Sum(A_ik * B_kj) for k from 1 to n

result = np.dot(A, B)
print("Matrix Multiplication \n", result)


print("=====================================")
# • Identity matrix

I = np.eye(6)
print("Identity Matrix \n", I)

print("=====================================")
# • Zero matrix

Z = np.zeros((2, 3))
print("Zero Matrix \n", Z)

print("=====================================")
# • Diagonal matrix

D = np.diag([1, 2, 3])
print("Zero Matrix \n", D)
