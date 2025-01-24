import numpy as np
P = np.array([[4, -9, 5],
              [-3,-1, 6],
              [9, -2,-6]]).reshape(3, 3)
B = np.array([[0, 4, 3],
              [-1,5, 3],
              [3,-4,-6]]).reshape(3, 3)
span_A = P @ B
a1 = span_A @ np.array([1,0,0])
a1 = a1.reshape(3,1)
a2 = span_A @ np.array([0,1,0])
a2 = a2.reshape(3,1)
a3 = span_A @ np.array([0,0,1])
a3 = a3.reshape(3,1)
print("a1 is:\n", a1, "\n")
print("a2 is:\n", a2, "\n")
print("a3 is:\n", a3)