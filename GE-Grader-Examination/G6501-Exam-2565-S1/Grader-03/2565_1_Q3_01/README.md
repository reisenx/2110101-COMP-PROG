<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Group Stage ★★ (
      <a href="https://drive.google.com/file/d/1F26AfX7ZdT7tbOQrNPDPe9K53HqM6b1w/view?usp=sharing">
        <code>2565_1_Q3_01</code>
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
# File Name : 2565_1_Q3_01.py
# Problem   : Group Stage
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

# Input teams and their country and store them in a dictionary
teams_country = {}
n = int(input())
for _ in range(n):
    team, country = input().split()
    teams_country[team] = country

# Input groups of teams and check if all teams in a group are from different countries
while True:
    # Input a group of teams or 'q' to quit
    group = input().strip().split()
    if group == ["q"]:
        break

    # Create a set to store unique countries in the group
    countries = set()
    for team in group:
        # Stop if a team is does not exist in the teams_country dictionary
        if team not in teams_country:
            break
        countries.add(teams_country[team])

    # Check if all teams in the group are from different countries
    if len(countries) == len(group):
        print("OK")
    else:
        print("Not OK")
```
