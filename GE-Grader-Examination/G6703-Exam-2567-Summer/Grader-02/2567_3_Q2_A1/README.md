<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Flowchart ★ (
      <a href="https://drive.google.com/file/d/1UziIdhFgHbr0cqfecQvGyEAKOLts1TO6/view?usp=sharing">
        <code>2567_3_Q2_A1</code>
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
# File Name : 2567_3_Q2_A1.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-07-31
# --------------------------------------------------

a, b, c, d = [int(num) for num in input().split()]

if a > b:
    if b < 0:
        c, d = d, c
    else:
        if b > 5:
            c -= d

        if b < 3:
            if b > 2:
                c //= d
            else:
                c *= d
        else:
            c += d
            c *= d

else:
    while a > d:
        b += 1
        a -= 1
        d += c

print(a, b, c, d)
```
