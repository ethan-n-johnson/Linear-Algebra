import numpy as np
import scipy.linalg as linalg
import matplotlib.pyplot as plt

X = np.random.randn(3, 4)

XTX = np.transpose(X) @ X

eigenvalues, eigenvectors = np.linalg.eig(XTX)

proj_eigenvectors = X@eigenvectors
norm_eigenvectors = proj_eigenvectors/np.linalg.norm(proj_eigenvectors, axis=0)

U, S, VT = np.linalg.svd(X, full_matrices=False)

print(U)
print(" ")
print(norm_eigenvectors)

# For U and the first three columns in norm_eigenvectors
# They contain the same values with different signs