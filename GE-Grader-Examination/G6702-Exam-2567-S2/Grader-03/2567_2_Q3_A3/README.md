<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Red ball ★☆ (
      <a href="https://drive.google.com/file/d/1xhNd3hF-0datqyz816erb_OIuLOHxJ79/view?usp=sharing">
        <code>2567_2_Q3_A3</code>
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
# File Name : 2567_2_Q3_A3.py
# Problem   : Red Ball
# Author    : Worralop Srichainont
# Date      : 2025-07-30
# --------------------------------------------------

# Input initial balls order
balls = input().strip().split(",")

# Swap balls operations
n = int(input())
for _ in range(n):
    # Input start and end indices for the swap operation in 1-based indexing
    start_idx, end_idx = [int(idx) for idx in input().split()]

    # Convert to 0-based indexing
    # NOTE: No need to decrement end_idx because the operation includes the end index
    start_idx -= 1

    # Swap the balls in range to the end of the list
    balls = balls[:start_idx] + balls[end_idx:] + balls[start_idx:end_idx]

# Output the final order of balls
print(",".join(balls))
```
