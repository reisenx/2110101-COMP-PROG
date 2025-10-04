<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Flowchart ★ (
      <a href="https://drive.google.com/file/d/1j65S2cZJpf_FsUE9_QZKgJipcFh5R8Xw/view?usp=sharing">
        <code>2567_2_Q2_A1</code>
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
# File Name : 2567_2_Q2_A1.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

a, b, c, d, e = [int(e) for e in input().split()]
if e == 1:
    if a < b:
        a, b = b, a
    if c < d:
        c, d = d, c
    if a >= c:
        if b >= c:
            print(b)
        else:
            print(c)
    else:
        if a >= b:
            print(a)
        else:
            print(d)
else:
    while e < 3:
        if a >= b:
            a, b = b, a
        if b >= c:
            b, c = c, b
        if c >= d:
            c, d = d, c
        e += 1
    print(b)
```
