<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Poker Hands ★★ (
      <a href="https://drive.google.com/file/d/1ybCeNooMRTp5wFQULhpAp9nw-TCpEhRa/view?usp=sharing">
        <code>2566_2_Q1_01</code>
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
# File Name : 2566_2_Q1_01.py
# Problem   : Poker Hands
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------

# Initialize the order of straight and flush
STRAIGHT = "AKQJX98765432A"
ROYAL_STRAIGHT = "AKQJX"
FLUSH = ["CCCCC", "HHHHH", "DDDDD", "SSSSS"]

n = int(input())
for _ in range(n):
    # Extract values and suits from the card set
    cards = input().strip("|")
    values = cards[::3]
    suits = cards[1::3]

    # Check the values and suits for straight and flush
    is_flush = suits in FLUSH
    is_straight = values in STRAIGHT
    is_royal_straight = values == ROYAL_STRAIGHT

    # Output the type of poker hand
    if is_royal_straight and is_flush:
        print("Royal Straight Flush")
    elif is_straight and is_flush:
        print("Straight Flush")
    elif is_straight:
        print("Straight")
    elif is_flush:
        print("Flush")
    else:
        print("None")
```
