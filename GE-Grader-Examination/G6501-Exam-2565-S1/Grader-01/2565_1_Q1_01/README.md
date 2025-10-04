<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Flowchart ★ (
      <a href="https://drive.google.com/file/d/1FXMD_zb9kZY0yza5yGkKEjzhIsln3957/view?usp=sharing">
        <code>2565_1_Q1_01</code>
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
# File Name : 2565_1_Q1_01.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

a, b, c, d = [int(e) for e in input().split()]
if a > b:
    a, b = b, a
    while d >= a:
        if c > d:
            a += 1
        else:
            d -= 1
else:
    if c % 2 == 0:
        d = d + a
    else:
        if d > c:
            c = c + d
        else:
            b = b + a
        a = b + c
print(a, b, c, d)
```
