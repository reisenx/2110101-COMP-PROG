<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Downsampling ★★ (
      <a href="https://drive.google.com/file/d/1cXqiNjkYF3NR1C04DxC9gApQuYIOjy5I/view?usp=sharing">
        <code>2567_1_Q3_B1-S</code>
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
# File Name : 2567_1_Q3_B1-S.py
# Problem   : Downsampling
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Input amount of numbers and initial time
n, initial_time = [int(num) for num in input().split()]

# Input numbers list
numbers = [float(num) for num in input().split()]

# Input k and command
data = input().strip().split()
k = int(data[0])
cmd = data[1].strip()

# Separate the numbers into chunks of size k and process them
for idx in range(0, len(numbers), k):
    # Calculate the current time of the current chunk
    current_time = initial_time + idx

    # Calculate the max and mean values for the current chunk
    max_value = max(numbers[idx : idx + k])
    mean_value = sum(numbers[idx : idx + k]) / len(numbers[idx : idx + k])

    # Output the result based on the command
    if cmd == "max":
        print(f"{current_time} {max_value}")
    elif cmd == "mean":
        print(f"{current_time} {round(mean_value, 2)}")
```
