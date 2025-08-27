# --------------------------------------------------
# File Name : 05_List_JTP.py
# Problem   : Interpolation
# Author    : Worralop Srichainont
# Date      : 2025-08-14
# --------------------------------------------------

# Input numbers a list of float
numbers = [float(num) for num in input().split()]

# Initialize after number interpolation process
interpolated_numbers = []

# Interpolate the numbers by inserting the average of each pair
for i in range(len(numbers) - 1):
    # Calculate the average of the current and next number
    avg_value = (numbers[i] + numbers[i + 1]) / 2

    # Append the current number and the average to the new list
    interpolated_numbers.append(numbers[i])
    interpolated_numbers.append(avg_value)
# Append the last number
interpolated_numbers.append(numbers[-1])

# Output the interpolated numbers
print(interpolated_numbers)
