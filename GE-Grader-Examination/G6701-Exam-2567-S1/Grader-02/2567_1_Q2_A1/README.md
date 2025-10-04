<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Flowchart ★ (
      <a href="https://drive.google.com/file/d/1oaR67Y1HE-or7eVXa--SdzR9SslRPY8P/view?usp=sharing">
        <code>2567_1_Q2_A1</code>
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
# File Name : 2567_1_Q2_A1.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

a, b, c, d = [int(e) for e in input().split()]
if a == 1:
    a = b + c + d
    if b > 5:
        if b > 9:
            c = 4 * d
        else:
            if b > 7:
                c = 5 * d
            else:
                c = 6 * d
    else:
        if b > 3:
            c = d
        else:
            if b > 0:
                c = 2 * d
            else:
                c = 3 * d
else:
    while b < c:
        b += 1
        if b > a:
            a += c
            c -= 1
        else:
            c -= 1
print(a, b, c, d)
```
