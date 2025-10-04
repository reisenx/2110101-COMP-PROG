<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Flowchart ★ (
      <a href="https://drive.google.com/file/d/1f3hgd5TDKZhNo-mKpnOi-fUeMvVRQkOZ/view?usp=sharing">
        <code>2567_2_Q1_A1</code>
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
# File Name : 2567_2_Q1_A1.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

a, b, c = [int(e) for e in input().split()]
if a < b:
    d = c
    x = "B"
    if c == 0:
        x = str(c) + x
    else:
        while c > 0:
            r = c % 2
            x = str(r) + x
            c = c // 2
    print(d, x)

else:
    if a > b:
        d = int(input())
        if a > c:
            a, b = b, a
            a, c = c, a
            a = a + 1
            b = b * 2

        if b > d:
            b, d = d, b
            a = a + 2
            b = b * 3

        c = a + (2 * b)
        d = c - (3 * a)
        print(a, b, c, d)
    else:
        e = float(input())
        f = float(input())
        out = e * (1 + (f / (100 * a))) ** (a * c)
        print(round(out, 2))
```
