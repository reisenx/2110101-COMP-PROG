<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Flowchart ★ (
      <a href="https://drive.google.com/file/d/1jhv8c59i_6af0xRp1c9lsiRnN2mYy4hB/view?usp=sharing">
        <code>2567_2_Q3_A1</code>
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
# File Name : 2567_2_Q3_A1.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-07-30
# --------------------------------------------------

a, b, c, d, e = [int(e) for e in input().split()]

if e >= 6:
    a = 1
    b = 1
    c = 0
    p = 10

    while abs(p - (b / a)) >= 10 ** (-e):
        p = b / a
        a, b = b, a + b
        c = c + 1

    print(b, c)

else:
    if a >= b:
        if c >= d:
            print(a + b + c + d)
        else:
            d, a, b, c = a, b, c, d
            print(a, b, c, d)
    else:
        e = (a * 3600) + (b * 60) + c + d
        e = e % (24 * 60 * 60)
        a = e // 3600
        b = (e - (a * 3600)) // 60
        c = e % 60

        print(a, b, c)
```
