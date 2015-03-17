"""
Homework 2a.
Demonstration script for quadratic interpolation.
"""

import numpy as np
import matplotlib.pyplot as plt

# Data points:
points = np.array([[-1., 0.], [1., 4.], [2., 3.]])
xi = points[:, 0]
yi = points[:, 1]

# Matrix A and vector b:
A = np.empty((3, 3))
for i in range(len(yi)):
    A[i, 0] = xi[i] ** 0
    A[i, 1] = xi[i] ** 1
    A[i, 2] = xi[i] ** 2    
b = yi

# Solve the system of linear equations:
C = np.linalg.solve(A, yi)

print "The polynomial coefficients are:"
print C


# Plot the resulting polynomial:
x = np.linspace(-2, 3, 1001)
y = C[0] + C[1] * x + C[2] * x**2

plt.figure(1)
plt.clf()
plt.plot(x, y, "b-")

# Add data points
plt.plot(xi, yi, "ro")

plt.ylim(-2,6)
plt.title("Data points and interpolating polynomial")
plt.savefig('hw2a.png') 

