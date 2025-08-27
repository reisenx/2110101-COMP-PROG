# --------------------------------------------------
# File Name : 11_NumPy_JTP.py
# Problem   : NumPy
# Author    : Worralop Srichainont
# Date      : 2025-08-15
# --------------------------------------------------

import numpy as np


# Multiply an array by a constant
def f1(arr, constant):
    return arr * constant


# Dot product of two vectors
def f2(vector_01, vector_02):
    return np.dot(vector_01, vector_02)


# Transpose a matrix
def f3(matrix):
    return matrix.T


# Calculate Alignment Vector
def f4(x, y, dx, dy, k, R):
    is_neighbors = ((x - x[k]) ** 2) + ((y - y[k]) ** 2) <= R**2

    sx = np.dot(is_neighbors, dx)
    sy = np.dot(is_neighbors, dy)

    t = np.arctan2(sy, sx)

    return np.cos(t), np.sin(t)


# Execute the input string as code
for _ in range(int(input())):
    exec(input().strip())
