# --------------------------------------------------
# File Name : 09_Nested_JTP.py
# Problem   : Convolution
# Author    : Worralop Srichainont
# Date      : 2025-08-15
# --------------------------------------------------


def convolute(a, b):
    # Find a number of matrix row and column
    rows = len(a)
    cols = len(a[0])

    # Calculate a convolute of matrix A and B
    total = 0
    for i in range(rows):
        for j in range(cols):
            total += a[i][j] * b[i][j]

    # Return a value
    return total


# Execute an input string as code
exec(input().strip())
