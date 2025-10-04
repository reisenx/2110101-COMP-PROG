<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Simple Expression Calculator ★★ (
      <a href="https://drive.google.com/file/d/1lVVt7vIHTU--47wxWlmma9nAeVPlxhKd/view?usp=sharing">
        <code>2565_1_Q1_03</code>
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
# File Name : 2565_1_Q1_03.py
# Problem   : Simple Expression Calculator
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

# Input equation and add spaces before operators
equation = ""
for char in input().strip():
    if char in "+-":
        equation += " "
    equation += char

# Split the equation string into numbers
numbers = []
for num in equation.split():
    numbers += [int(num)]

# Calculate the sum of the numbers and print the result
print(sum(numbers))
```
