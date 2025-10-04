<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Credit Points ★★ (
      <a href="https://drive.google.com/file/d/1i2hhun44grSnF-DZH80CKTKjj4O4ch3m/view?usp=sharing">
        <code>2566_2_Q2_02</code>
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
# File Name : 2566_2_Q2_02.py
# Problem   : Credit Points
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------

# Initialize dictionaries to store coupon details and usage
coupons_details = {}
coupons_usage = {}

# Read the number of coupons and their prices
n = int(input())
for _ in range(n):
    name, price = input().strip().split()
    coupons_details[int(price)] = name

# Input the total point available and initialize remaining points and used points
total_points = int(input())
remain_points = total_points
used_points = 0

# Sort the coupons by price in descending order and calculate usage
sorted_coupons_details = sorted(coupons_details.items())[::-1]
# Loop through the sorted coupons and calculate how many can be used
for price, name in sorted_coupons_details:
    # Spent points only if there are enough remaining points
    if remain_points >= price:
        # Calculate amount of coupon that can be used
        usage = min(remain_points // price, 3)
        # Update the usage and remaining points
        coupons_usage[name] = usage
        remain_points -= usage * price
        used_points += usage * price

# Output the total points, used points, and remaining points
print(f"> {total_points} {used_points} {remain_points}")
# Output the coupons and their usage sorted by name alphabetically
if used_points == 0:
    print("No coupon")
for name, usage in sorted(coupons_usage.items()):
    print(name, usage)
```
