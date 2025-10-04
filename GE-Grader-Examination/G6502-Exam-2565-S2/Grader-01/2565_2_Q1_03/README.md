<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Flowchart ★ (
      <a href="https://drive.google.com/file/d/1saNRhE1lTJyWSRQTbPN6nIesX0kRGOx1/view?usp=sharing">
        <code>2565_2_Q1_03</code>
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
# File Name : 2565_2_Q1_03.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

a, b, c, d = [int(e) for e in input().split()]

if d > a:
    n = 0
    while a < d:
        n = n + 1
        a = a + abs(b)
        d = d - abs(c)
    print(n, a, d)
else:
    a, d = d, a
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    if b == c:
        print(a, b, d)
    else:
        if b > c:
            print((b + c) / 2)
        else:
            print(a, b, c, d)
```
