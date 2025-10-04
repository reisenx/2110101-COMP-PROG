<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Lyla ★★ (
      <a href="https://drive.google.com/file/d/1GhTOX-xn20MxpVoo8Q9_AnJzXfbU0CWA/view?usp=sharing">
        <code>2567_2_Q2_A2</code>
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
# File Name : 2567_2_Q2_A2.py
# Problem   : Lyla
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Initializing time, displacement, and velocity variables
time = 0
displacement = [0.0, 0.0]
velocity = [0.0, 0.0]

# Input acceleration and displacement
data = [float(e) for e in input().split()]
acceleration = [data[0], data[1]]
displacement[1] = data[2]

# Check if the acceleration of the hunter is more than the acceleration of the prey
if acceleration[0] > acceleration[1]:
    # Loop until the hunter catches the prey
    while displacement[1] > displacement[0]:
        # Increment time
        time += 1

        # Update displacement
        displacement[0] += velocity[0] + (0.5 * acceleration[0])
        displacement[1] += velocity[1] + (0.5 * acceleration[1])

        # Update velocity
        velocity[0] += acceleration[0]
        velocity[1] += acceleration[1]

    # Output the time and displacement of the hunter when he catches the prey
    print(time, round(displacement[0], 2))

# If the acceleration of the hunter is not greater than the prey's,
# it's not possible to catch the prey
else:
    print("Not possible")
```
