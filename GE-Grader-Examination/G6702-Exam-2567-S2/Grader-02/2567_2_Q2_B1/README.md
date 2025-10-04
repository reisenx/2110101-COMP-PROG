<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    List Rearragement 2 ★★ (
      <a href="https://drive.google.com/file/d/1g1L5WnvX83lrKPCAEQFQQbIM8RMDpLfe/view?usp=sharing">
        <code>2567_2_Q2_B1</code>
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
# File Name : 2567_2_Q2_B1.py
# Problem   : List Rearrangement 2
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------


# Returns a new position list based on the input numbers
def find_P(numbers):
    # Initialize an empty list to store positions
    positions = []

    # Reverse the input numbers and rearrange them
    reversed_numbers = numbers[::-1]
    for i in range(len(reversed_numbers)):
        # If the index is even, append to the end
        if i % 2 == 0:
            positions.append(reversed_numbers[i])

        # If the index is odd, insert at the beginning
        else:
            positions.insert(0, reversed_numbers[i])

    # Return the rearranged positions
    return positions


# Rearranges the input list based on the positions calculated from find_P
def rearrange(numbers):
    # Initialize an empty list to hold the rearranged numbers
    rearranged_numbers = []
    # Get the positions from the find_P function
    positions = find_P(numbers)
    # Initialize the position counter
    pos = 0

    # Rearrange the numbers based on the positions
    for add_position in positions:
        # Calculate the new position and index in the original list
        pos += add_position
        idx = pos % len(numbers)

        # Append the number at the calculated index to the rearranged list
        rearranged_numbers.append(numbers[idx])
        # Remove the current number from the original list
        numbers.pop(idx)

    # Return the rearranged numbers
    return rearranged_numbers


# Execute the input string as code
exec(input().strip())
```
