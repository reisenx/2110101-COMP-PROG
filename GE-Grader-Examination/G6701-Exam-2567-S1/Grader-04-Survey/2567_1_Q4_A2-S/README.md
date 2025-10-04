<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Sales Revenue ★☆ (
      <a href="https://drive.google.com/file/d/1dtHz7HJZBxXfQWcV1qD4toB7S1Lekbwi/view?usp=sharing">
        <code>2567_1_Q4_A2-S</code>
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
# File Name : 2567_1_Q4_A2-S.py
# Problem   : Sales Revenue
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Input benefits percentage for each type
BENEFITS = [0.0, 0.0, 0.0, 0.0]
for i in range(4):
    BENEFITS[i] = float(input().strip()) / 100

# Initialize total benefit money
total_benefit = 0.0

# Input sales records
n = int(input().strip())
for _ in range(n):
    # Extract sales type and money gained
    data = input().strip().split()
    type = int(data[1]) - 1
    sales = float(data[2])

    # Calculate benefit for this sale and add to total
    total_benefit += BENEFITS[type] * sales

# Output total benefit rounded to 2 decimal places
print(round(total_benefit, 2))
```
