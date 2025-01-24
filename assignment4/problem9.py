import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rotation_matrix(angle):
    angle = np.deg2rad(angle)
    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)
    # Define the 4x4 rotation matrix for the x-axis
    R = np.array([[1, 0, 0, 0],
                  [0, cos_angle, -sin_angle, 0],
                  [0, sin_angle, cos_angle, 0],
                  [0, 0, 0, 1]])
    return R

def translation_matrix(x, y, z):
    return np.array([[1, 0, 0, x],
                     [0, 1, 0, y],
                     [0, 0, 1, z],
                     [0, 0, 0, 1]])

# Translate from (1, -2, 2) to origin
T1 = translation_matrix(1, -2, 2)
# Rotate
R = rotation_matrix(-90)
# Translate from origin to (1, -2, 2)
T2 = translation_matrix(-1, 2, -2)
# Multiply all of the transformations
T = T2 @ R @ T1

point = np.array([1, 2, 1, 1])
x_trans = T @ point;
T_inv = np.linalg.inv(T)
# Reverse the Transform by multiplying by the inverse
x_rev = T_inv @ x_trans

fig3d = plt.figure()
ax3d = fig3d.add_subplot(projection='3d')
ax3d.set_xlim([-9, 9])
ax3d.set_ylim([-9, 9])
ax3d.set_zlim([-9, 9])
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')

ax3d.scatter(point[0], point[1], point[2], color='r', s=100, label='Original Point')
ax3d.scatter(x_trans[0], x_trans[1], x_trans[2], color='b', s=100, label='Transformed Point')
ax3d.scatter(x_rev[0], x_rev[1], x_rev[2], color='g', s=100, label='Reversed Transform Point')
plt.show()