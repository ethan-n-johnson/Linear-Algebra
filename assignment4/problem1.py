import numpy as np
import sympy
import scipy.linalg as linalg

A = np.array([[0, 2, 3], 
              [1, 1, -2], 
              [4, 1, 0], 
              [3, -1, -1]])

A_rank = np.linalg.matrix_rank(A)
# Get the RREF of matrix A and store it in A_rref and store the indices of the pivots in columns
A_rref, columns = sympy.Matrix(A).rref()
# Find the basis by of the column space of A by selecting all rows (:) and only the columns in the columns variable
A_basis = A[:, list(columns)]
print(A_rank)
print(A_basis)