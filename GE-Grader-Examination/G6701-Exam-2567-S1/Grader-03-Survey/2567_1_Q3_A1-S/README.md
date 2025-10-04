<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Flowchart ★ (
      <a href="https://drive.google.com/file/d/130S4U4hoYa6hQNmiH0_6BSWmG5HP_ZOA/view?usp=sharing">
        <code>2567_1_Q3_A1-S</code>
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
# File Name : 2567_1_Q3_A1-S.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

a, b, c, d = [int(e) for e in input().split()]

if a == 1:
    a = b + c + d
    if b == 1:
        c += c + d
    else:
        if b > 4:
            c += c * d
        if b > 5:
            c += c % d
    print(c)
else:
    while b < c:
        b += 1
        if b > a:
            break
print(a, b, c, d)
```
