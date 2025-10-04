<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Repeat Count ★★ (
      <a href="https://drive.google.com/file/d/1QM3JjWkZ2QuDEAW3o9mUNCqXGzSTJ0gZ/view?usp=sharing">
        <code>2566_2_Q1_03</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**Solution 1**](#solution-1)
-   [**Solution 2**](#solution-2)

---

<div align="center">
  <h2>เฉลยอย่างละเอียดจะตามมาทีหลัง</h2>
</div>

---

# Solution 1

```python
# --------------------------------------------------
# File Name : 2566_2_Q1_03-sol1.py
# Problem   : Repeat Count
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------


# Count the number of times a pattern repeats in a text
def get_repeat_count(text, pattern):
    # Initialize the repeat as maximum possible repeats
    repeat = len(text) // len(pattern)
    # Decrease the repeat count until the pattern is found
    while repeat > 1:
        if pattern * repeat in text:
            return repeat
        repeat -= 1
    # If no repeat found, return 0
    return 0


# Read the pattern and the number of test cases
pattern = input().strip()
n = int(input())
# Read each test case and output the repeat count
for _ in range(n):
    text = input().strip()
    print(get_repeat_count(text, pattern))
```

---

# Solution 2

```python
# --------------------------------------------------
# File Name : 2566_2_Q1_03-sol2.py
# Problem   : Repeat Count
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------


# Count the number of times a pattern repeats in a text
def get_repeat_count(text, pattern):
    # Initialize the index and repeat count
    idx = 0
    repeat = 0
    max_repeat = 0
    # Iterate through the text to find the pattern
    while idx < len(text):
        # If the pattern is found, increase the repeat count
        # and move the index forward by the length of the pattern
        if text[idx : idx + len(pattern)] == pattern:
            repeat += 1
            idx += len(pattern)
        # If the pattern is not found, check if we have a maximum repeat
        # and reset the repeat count
        else:
            max_repeat = max(max_repeat, repeat)
            repeat = 0
            idx += 1
    # Do not forget to check the last repeat count
    max_repeat = max(max_repeat, repeat)

    # Return the maximum repeat count if greater than 1
    if max_repeat > 1:
        return max_repeat
    # If no repeat found, repeat count is 0
    return 0


# Read the pattern and the number of test cases
pattern = input().strip()
n = int(input())
# Read each test case and output the repeat count
for _ in range(n):
    text = input().strip()
    print(get_repeat_count(text, pattern))
```
