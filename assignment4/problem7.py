import numpy as np
import sympy
import scipy.linalg as linalg
def rotation_matrix(angle, axis):
    angle = np.deg2rad(angle)
    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)
    # Define the rotation matrix for the X-Axis
    if(axis == 'x'):
        R = np.array([[1, 0, 0],
                      [0,cos_angle, -sin_angle],
                      [0,sin_angle,cos_angle]])
    # Define the rotation matrix for the Y-Axis
    elif(axis == 'y'):
        R = np.array([[cos_angle, 0, sin_angle],
                      [0, 1, 0],
                      [-sin_angle,0,cos_angle]])
    # Define the rotation matrix for the Z-Axis
    elif(axis == 'z'):
        R = np.array([[cos_angle, -sin_angle, 0],
                      [sin_angle,cos_angle, 0],
                      [0,0,1]])
    return R