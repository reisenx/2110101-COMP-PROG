<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Decryption ★★ (
      <a href="https://drive.google.com/file/d/13yV-9L1WZIbXhRva2IoDF_BxYCrykC7h/view?usp=sharing">
        <code>2565_2_Q1_01</code>
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
# File Name : 2565_2_Q1_01.py
# Problem   : Decryption
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------


# Rotate a string to the left by n positions
def rotate_left(num, n):
    idx = n % len(num)
    return num[idx:] + num[:idx]


# Rotate a string to the right by n positions
def rotate_right(num, n):
    idx = len(num) - (n % len(num))
    return num[idx:] + num[:idx]


# Modulo each digit of a string by a given modulus
def str_mod(num, mod):
    result = ""
    for digit in num:
        result += str(int(digit) % mod)
    return result


# Main function
def main():
    # Input a string of digits
    number = input().strip()
    # Extract the last two digits as command and n
    cmd = int(number[-2])
    n = int(number[-1])

    # Rotate left number by n positions
    if cmd == 1:
        number = rotate_left(number, n)
    # Rotate right number by n positions
    elif cmd == 2:
        number = rotate_right(number, n)
    # Modulo each digit of number by n
    elif cmd == 3:
        number = str_mod(number, n)
    # Output
    print(number)


# Execute a input string as code
exec(input().strip())
```
