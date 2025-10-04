<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Scout ★★ (
      <a href="https://drive.google.com/file/d/1cST70loS_Wfreh2mwh7RSmKwLeR216ZH/view?usp=sharing">
        <code>2567_3_Q1_A2</code>
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
# File Name : 2567_3_Q1_A2.py
# Problem   : Boy Scouts
# Author    : Worralop Srichainont
# Date      : 2025-07-31
# --------------------------------------------------

import math

# Input boys names
boys = input().strip().split()

# Input group size and calculate the number of groups
group_size = int(input())
group_amount = math.ceil(len(boys) / group_size)

# Input group names and multiply them by the group size
group_names = []
for _ in range(group_amount):
    group_names += [input().strip()] * group_size

# Input names to query
query_names = input().strip().split()

# For each queried name, find the corresponding group name
query_results = []
for name in query_names:
    idx = boys.index(name)
    query_results.append(group_names[idx])

# Output the group names for the queried names
print(" ".join(query_results))
```
