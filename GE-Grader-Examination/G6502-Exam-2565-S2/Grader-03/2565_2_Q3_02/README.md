<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Seating Map ★☆ (
      <a href="https://drive.google.com/file/d/18G-CQOFTieLXVpGkQaB3E-3rvsJKQNLY/view?usp=sharing">
        <code>2565_2_Q3_02</code>
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
# File Name : 2565_2_Q3_02.py
# Problem   : Seating Map
# Author    : Worralop Srichainont
# Date      : 2025-07-12
# --------------------------------------------------


# Print the seating assignments in a formatted way
def print_seats(assignments, n_rows, n_cols):
    # Create a 2D list to represent the seating map
    seats = [["| -- "] * n_cols for _ in range(n_rows)]
    # Fill the seating map with the names from the assignments
    for name, pos in assignments:
        # Calculate the row and column based on the position
        r = (pos - 1) // n_cols
        c = (pos - 1) % n_cols
        # Place the name in the correct position in the seating map
        seats[r][c] = f"| {name} "

    # Print the seating map
    for row in seats:
        print("".join(row) + "|")


# Execute a input string as code
exec(input().strip())
```
