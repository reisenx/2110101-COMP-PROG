# --------------------------------------------------
# File Name : 06_Func_JTP.py
# Problem   : Status and Faculty
# Author    : Worralop Srichainont
# Date      : 2025-08-14
# --------------------------------------------------

# Initialize constants
UNDERGRAD_DIGITS = ["0", "3", "4"]
FACULTY_CODES = [["21", "ENG"], ["22", "ART"], ["23", "SCI"]]


# Check if the student is undergraduate student
def is_undergrad(student_id):
    return student_id[2] in UNDERGRAD_DIGITS


# Get faculty of the student
def get_faculty(student_id):
    for code, faculty in FACULTY_CODES:
        if student_id[-2] == code:
            return faculty
    return "OTHER"


# Get type and faculty of the student
def get_status(student_id):
    # Initialize result list
    result = []

    # Check if the student is undergraduate or graduate
    if is_undergrad(student_id):
        result.append("U")
    else:
        result.append("G")

    # Append faculty of the student
    result.append(get_faculty(student_id))

    # Return the result
    return result
