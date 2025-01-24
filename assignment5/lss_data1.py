import numpy as np
import scipy.linalg as linalg
import matplotlib.pyplot as plt


data = np.loadtxt('assignment5/dataset1.txt')

x = data[:, 0]
y = data[:, 1]

A = np.vstack([x, np.ones(len(x))]).T

slope, intercept = np.linalg.lstsq(A, y, rcond=None)[0]

plt.scatter(x, y, label="Points", color="black")
plt.plot(x, slope * x + intercept, label=f"Linear Least Squares Solution Graph", color="blue")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()