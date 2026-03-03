# Introduction to Matrix Decomposition
# • What is Matrix Decomposition?
#   • Process of breaking a matrix into simpler components to analyze or solve problems
#   • Singular Value Decomposition (SVD)
#   • SVD decomposes a matrix A A into three matrices: A = U • £ • VT
#     • U: Left singular vectors (orthogonal matrix)
#     • L: Diagonal matrix of singular values (non-negative).
#     • VT: Right singular vectors (orthogonal matrix).
# • Applications of SVD
# • Computing SVD in NumPy


import numpy as np

A = np.array([[2, 3], [1, 4]])

U, S, Vt = np.linalg.svd(A)
print("U: \n", U)
print("Singular Values: \n", S)
print("V Transpose: \n", Vt)
