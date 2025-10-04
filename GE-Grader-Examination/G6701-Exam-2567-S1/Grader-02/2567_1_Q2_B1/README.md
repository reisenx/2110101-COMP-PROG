<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    List Rearrangement ★★ (
      <a href="https://drive.google.com/file/d/1Rx2OWmHmJHDPIgUdRF2nwEdlr3RrBEnL/view?usp=sharing">
        <code>2567_1_Q2_B1</code>
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
# File Name : 2567_1_Q2_B1.py
# Problem   : List Rearrangement
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input a list of numbers
numbers = [int(num) for num in input().split()]

# Create another sequence of sorted numbers
sorted_numbers = sorted(numbers)

# Initialize an empty list to hold the rearranged numbers
rearranged_numbers = []
# Initialize the position counter
position = 0

# Rearrange the numbers based on the sorted sequence
for add_position in sorted_numbers:
    # Calculate the new position in the original list
    position += add_position
    # Get the index in the original list
    idx = position % len(numbers)

    # Append the number at the calculated index to the rearranged list
    rearranged_numbers.append(str(numbers[idx]))
    # Remove the number from the original list
    numbers.pop(idx)

# Output the rearranged numbers
print(" ".join(rearranged_numbers))
```
