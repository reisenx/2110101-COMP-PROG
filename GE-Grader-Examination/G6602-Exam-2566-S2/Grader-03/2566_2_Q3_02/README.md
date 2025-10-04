<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Friends ★★ (
      <a href="https://drive.google.com/file/d/1_I8h_pHSZyKAuHf4Xf_KONQZnPnCFmD_/view?usp=sharing">
        <code>2566_2_Q3_02</code>
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
# File Name : 2566_2_Q3_02.py
# Problem   : Friends
# Author    : Worralop Srichainont
# Date      : 2025-07-15
# --------------------------------------------------


# Read relationship data and return a list of tuples.
def read_friends():
    friends = []
    n = int(input())
    for _ in range(n):
        friends.append(tuple(input().strip().split()))
    return friends


# Count the number of friends for each person in the list of names.
def count_friends(friends, names):
    # Create a dictionary to store set of friends of each person.
    all_friends = {}
    for a, b in friends:
        # Initialize the sets for each person if they do not exist.
        if a not in all_friends:
            all_friends[a] = set()
        if b not in all_friends:
            all_friends[b] = set()
        # Add each person to the other's set of friends.
        all_friends[a].add(b)
        all_friends[b].add(a)

    # Sort the names and count the number of friends for each.
    result = []
    for name in sorted(names):
        # If the name is not in the dictionary, they have no friends.
        if name not in all_friends:
            result.append((name, 0))
        # Otherwise, append the name and the count of friends.
        else:
            result.append((name, len(all_friends[name])))
    # Return the sorted list of tuples with names and their friend counts.
    return result


# Execute the input string as code
exec(input().strip())
```
