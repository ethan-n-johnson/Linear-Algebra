import numpy as np
import sympy
import scipy.linalg as linalg

# Set up matrices
A = np.array([4, 8, -5, -3, -6, -7, 2, 4, 2])
A = A.reshape(3,3)
b = np.array([-1, -1, 3])
b = b.reshape(3,1)

# Print matrices
print(A)
print(b)
print("\n")

# Compute RREF and convert back to numpy
A_sympy = sympy.Matrix(A)
A_rref = A_sympy.rref()
A_np = np.array(A_rref[0].tolist())
print(A_np)

# Column space of A
colA = A_sympy.columnspace();
print(colA)
# Solve equation Ax = b
x = linalg.solve(A, b)
# the matrix is singular
print(x)
# Null space of A
nullA = linalg.null_space(A)
print(nullA)