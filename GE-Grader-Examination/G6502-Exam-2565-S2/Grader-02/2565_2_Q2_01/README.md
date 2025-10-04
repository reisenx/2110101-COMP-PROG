<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Small Lot First ★★ (
      <a href="https://drive.google.com/file/d/1amVihMObcBwSYfZxmxeAXNxFKbRssTFi/view?usp=sharing">
        <code>2565_2_Q2_01</code>
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
# File Name : 2565_2_Q2_01.py
# Problem   : Small Lot First
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

# Input the total money available
total_money = int(input())

# Input the customers and their reserved money
customers = []
while True:
    data = input().strip()
    # Break if the input is "Q"
    if data == "Q":
        break
    # Append customer data to the list
    name, reserved = data.split()
    customers.append([name, 0, int(reserved)])

# Initialize the index of the current customer
idx = 0

# Distribute the money to customers in a round-robin fashion
while total_money > 0:
    # Extract the current customer's data
    current_money, reserved = customers[idx][1:]
    # If the current customer has less money than reserved, give them 1 unit of money
    if current_money < reserved:
        customers[idx][1] += 1
        total_money -= 1
    # Move to the next customer
    idx = (idx + 1) % len(customers)

# Output the final money for each customer
for name, current_money, _ in customers:
    print(name, current_money)
```
