from os import PRIO_PGRP

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import solve


def plot_lines(matrix):
    import numpy as np
    import matplotlib.pyplot as plt

    # Generate x values for plotting
    x = np.linspace(-10, 10, 100)

    # Loop through each row in the matrix
    for row in matrix:
        a, b, c = row
        if b != 0:
            plt.plot(x, (c - a * x) / b, label=f'{a}x + {b}y = {c}')
        else:
            plt.axvline(-c / a, label=f'{a}x = {c}')

    # Add gridlines, axis labels, and legend
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

# Creating an arrays
# A = np.array([[-1,3],[3,2]], dtype= np.dtype(float))
# B = np.array([7,1],dtype=np.dtype(float))
# print(f"Matrix A: {A}")
# print(f"Array B: {B}")

# Printing the shape
# print(f"Shape of A: {A.shape}")
# print(f"Shape of B: {B.shape}")

# Solve the system of equations
# x = np.linalg.solve(A, B)
# print(f"Solution to the system: {x}")

#  Calculate the determinant of A
# d = np.linalg.det(A)
# print(f"{d:.2f}")

# Stacking A and B horizontally
# A_system = np.hstack((A,B.reshape((2,1))))
# # print(A_system)
#
# #  Extracting the second row
# # print(A_system[1])
#
# # Visualizing the system of equations
# plot_lines(A_system)

#  New matrix A_2 and vector B_2
A_2 = np.array([
    [-1,3],
    [3,-9]
], dtype=np.dtype(float))
B_2 = np.array([7,1],dtype=np.dtype(float))
# print(A_2)
# print(B_2)

# Calculate the determinan of A_2
d_A2 = np.linalg.det(A_2)
print(f"{d_A2:2f}")
#
try:
    x_2 = np.linalg.solve(A_2,B_2)
except np.linalg.LinAlgError as err:
    print(err)
