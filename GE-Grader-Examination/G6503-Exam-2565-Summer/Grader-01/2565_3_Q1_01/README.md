<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Flowchart ★ (
      <a href="https://drive.google.com/file/d/1okyp4jXo4Mj19ytxDZ4KQsSRT3sTF2Mk/view?usp=sharing">
        <code>2565_3_Q1_01</code>
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
# File Name : 2565_3_Q1_01.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-07-12
# --------------------------------------------------

a, b, c = [int(e) for e in input().split()]

if abs(a) > abs(b):
    r, s = 0, 0
    ta = abs(a)
    tb = abs(b)
    while ta > tb:
        ta = ta - tb
        s = s + 1
    r = ta
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        pass
    else:
        s = -s
        r = -r
    print(a, b, s, r)
else:
    if (b > 0 and c > 0) or (b < 0 and c < 0):
        p = 0
        tc = abs(c)
        for _ in range(tc):
            p = p + abs(b)
    else:
        p = abs(b)
        tc = abs(c)
        while tc > 0:
            p = p + abs(b)
            tc = tc - 1
        p = -(p - abs(b))
    print(b, c, p)
```
