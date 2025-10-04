<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Graduation Ceremony ★★★ (
      <a href="https://drive.google.com/file/d/1WBB8TOkW_fw3vlitH2TXXcxpklcce0la/view?usp=sharing">
        <code>2565_1_Q3_02</code>
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
# File Name : 2565_1_Q3_02.py
# Problem   : Graduation Ceremony
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

# Input number of students, faculties, and testcases
student_count, guest_count, testcases = [int(amt) for amt in input().split()]

# Create a dictionary to map students to their faculty
students_faculty = {}
for _ in range(student_count):
    student, faculty = input().split()
    students_faculty[student] = faculty

# Create a dictionary to map each guest to the set of faculties of their students
guest_faculties = {}
for _ in range(guest_count):
    # Read the guest name and their visited students
    people = input().split()
    guest = people[0]
    students = people[1:]

    # Create a set of faculties for the visited students of each guest
    faculties = set()
    for student in students:
        faculties.add(students_faculty[student])
    # Store the faculties in the guest_faculties dictionary
    guest_faculties[guest] = faculties

# Process each testcase to find the common faculties among the guests
for _ in range(testcases):
    # Read the guests for this testcase
    guests = input().split()

    # Find the common faculties among the guests
    result = guest_faculties[guests[0]]
    for guest in guests[1:]:
        result &= guest_faculties[guest]

    # Output the common faculties alphabetically
    if len(result) > 0:
        print(" ".join(sorted(result)))
    else:
        print("None")
```
