import numpy as np
import scipy.linalg as linalg
import matplotlib.pyplot as plt

A = np.array([[1, -2],
              [-4, 1]])

eigenvalues, eigenvectors = np.linalg.eig(A)

fig, ax = plt.subplots()

ax.set_xlim([-5, 4])
ax.set_ylim([-5, 4])
ax.set_aspect('equal', 'box')
ax.set_xlabel('X')
ax.set_ylabel('Y')

ax.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1, color='r', label='Standard Basis vector 1')
ax.quiver(0, 0, 0, 1, angles='xy', scale_units='xy', scale=1, color='b', label='Standard Basis vector 2')

ax.quiver(0, 0, A[0, 0], A[1, 0], angles='xy', scale_units='xy', scale=1, color='g', label='A vector 1')
ax.quiver(0, 0, A[0, 1], A[1, 1], angles='xy', scale_units='xy', scale=1, color='g', label='A vector 2')

ax.quiver(0, 0, eigenvectors[0, 0], eigenvectors[1, 0], angles='xy', scale_units='xy', scale=1, color='black', label='eigenvector 1')
ax.quiver(0, 0, eigenvectors[0, 1], eigenvectors[1, 1], angles='xy', scale_units='xy', scale=1, color='black', label='eigenvector 2')

ax.legend()
plt.show()