<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Students in Course ★★ (
      <a href="https://drive.google.com/file/d/1RaqjKrdRqYq1Q_4bk1QxuT5OdIz_muvG/view?usp=sharing">
        <code>2567_1_Q3_C2-S</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**Solution**](#solution)

---

<div align="center">
  <h2>เฉลยอย่างละเอียดจะตามมาทีหลัง</h2>
</div>

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q3_C2-S.py
# Problem   : Students in Subjects
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Initialize a dictionary to store subjects and their registration information
subjects_registration = {}

# Input the number of students
n = int(input())

# Input student student registration data
for _ in range(n):
    # Extract student ID and subjects they are registered for from input
    data = input().strip().split()
    student_id = data[0].strip()
    subjects = data[1:]

    # Concatenate the digits from the student ID with '25' to form the academic year
    academic_year = f"25{student_id[:2]}"

    # Update each subject to the dictionary
    for subject in subjects:
        # Initialize the subject in the dictionary if not already exists
        if subject not in subjects_registration:
            subjects_registration[subject] = {}

        # Initialize the academic year in the subject's dictionary if not already exists
        if academic_year not in subjects_registration[subject]:
            subjects_registration[subject][academic_year] = 0
        # Increment the count of the current academic year for the current subject
        subjects_registration[subject][academic_year] += 1

# Input query subjects
query_subjects = input().strip().split()

# Iterate through each query subject
for subject in query_subjects:
    # Check if the subject exists in the registration dictionary
    if subject in subjects_registration:
        # Initialize a list to store the years and their counts
        year_enrolled = []

        # Sort the years and format them with their counts
        for year, count in sorted(subjects_registration[subject].items()):
            year_enrolled.append(f"{year}:{count}")

        # Output the subject with the years and their counts
        print(f"{subject} {', '.join(year_enrolled)}")

    # If the subject does not exist, print the subject with 'None'
    else:
        print(f"{subject} None")
```
