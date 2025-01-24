import numpy as np
import sympy
import scipy.linalg as linalg

# Calculate the orthonormal basis
def orthonormal_basis(A):
    rows, columns = A.shape
    M = np.zeros(rows,columns)

    # gram-schmidt
    for i in range(columns):
        v = A[:, i].copy()
        for j in range(i):
            proj = np.dot(A[:, i], M[:, j])
            v = v-proj*M[:, j]

    # Normalize
    norm = np.sqrt(np.dot(v,v))
    M[:, j] = v/norm
    
    return M