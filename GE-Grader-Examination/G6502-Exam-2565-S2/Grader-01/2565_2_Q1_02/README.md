<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    AQI ★☆ (
      <a href="https://drive.google.com/file/d/1Kx2j8XuotCYUap1uBYRM5UWArRnfnSv0/view?usp=sharing">
        <code>2565_2_Q1_02</code>
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
# File Name : 2565_2_Q1_02.py
# Problem   : Air Quality Index (AQI)
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

# Input
aqi = [int(e) for e in input().split()]

# Output
print("AQI|1 2 3 4 5")
print("-------------")
for i in range(7):
    if aqi[i] < 25:
        print(f"{i + 1}..|+........")
    elif 25 <= aqi[i] < 50:
        print(f"{i + 1}..|..+......")
    elif 50 <= aqi[i] < 100:
        print(f"{i + 1}..|....+....")
    elif 100 <= aqi[i] < 200:
        print(f"{i + 1}..|......+..")
    elif aqi[i] >= 200:
        print(f"{i + 1}..|........+")
print("-------------")
```
