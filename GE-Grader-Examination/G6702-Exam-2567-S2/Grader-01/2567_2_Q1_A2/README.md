<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Temperature Change ★★ (
      <a href="https://drive.google.com/file/d/1j7D-tr5qBp5H0i1LItXGmxd--MQF71QW/view?usp=sharing">
        <code>2567_2_Q1_A2</code>
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
# File Name : 2567_2_Q1_A2.py
# Problem   : Temperature Change
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Initialization of constants
K1 = [0.05, 0.02, 0.01, 0.015]
K2 = [1.5, 1.0, 0.8]

# Input temperatures information
temp_old = float(input())
temp_room = float(input())

# Input time interval
time_interval = float(input())

# Input material and wind type
material_type = int(input())
wind_type = int(input())

# Calculate k constant by material and wind type
k = K1[material_type - 1] * K2[wind_type - 1]

# Initialize total time and new temperature
total_time = time_interval
temp_new = temp_old - k * (temp_old - temp_room) * time_interval

# Calculate the time until the temperature difference is less than 0.001
while abs(temp_old - temp_new) >= 10**-3:
    # Update total time
    total_time += time_interval

    # Update temperatures
    temp_old = temp_new
    temp_new = temp_old - k * (temp_old - temp_room) * time_interval

# Output the total time and the final temperature
print(round(total_time, 2), round(temp_new, 3))
```
