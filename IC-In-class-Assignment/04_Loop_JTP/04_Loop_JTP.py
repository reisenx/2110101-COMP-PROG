# --------------------------------------------------
# File Name : 04_Loop_JTP.py
# Problem   : Average Grade
# Author    : Worralop Srichainont
# Date      : 2025-08-14
# --------------------------------------------------

# Initialize the grade letters and its value
GRADE_LETTER = ["A", "B", "C", "D", "F"]
GRADE_VALUE = [4.0, 3.0, 2.0, 1.0, 0.0]

# Initialize total grade value
total_value = 0.0

# Input grade and calculate total value
grades = input().strip().split()
for grade in grades:
    idx = GRADE_LETTER.index(grade)
    total_value += GRADE_VALUE[idx]

# Calculate average grade
average_grade = total_value / len(grades)

# Output average grade
print(round(average_grade, 2))
