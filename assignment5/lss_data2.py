import numpy as np
import scipy.linalg as linalg
import matplotlib.pyplot as plt


data = np.loadtxt('assignment5/dataset2.txt')

x = data[:, 0]
y = data[:, 1]

A = np.vstack([x**2, x, np.ones(len(x))]).T

a, b, c = np.linalg.lstsq(A, y, rcond=None)[0]

plt.scatter(x, y, label="Points", color="black")
plt.plot(x, a * x**2 + b*x + c, label=f"Quadratic Least Squares Solution Graph", color="blue")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()