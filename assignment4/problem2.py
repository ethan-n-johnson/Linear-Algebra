import numpy as np
import sympy
import scipy.linalg as linalg
# Matrix multiply the change of basis matrix by the vector whos basis you want changed
def change_basis(cob_matrix, vector):
    changed_vector = cob_matrix @ vector
    return changed_vector

B = np.array([[0, -4, 6],
              [-1, 0, 6],
              [-1, 0, 3]])

x = np.array([-18, 8, 5]).reshape(-1, 1)
x_B = np.array([-2, 6, 1]).reshape(-1, 1)
# Call the change basis function to change x's basis to B
print(change_basis(B, x))
# Call the change basis function to change x_B's basis to the standard basis
print(change_basis(B, x_B))