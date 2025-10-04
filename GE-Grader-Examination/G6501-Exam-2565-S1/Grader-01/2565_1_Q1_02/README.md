<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Multiplexer ★☆ (
      <a href="https://drive.google.com/file/d/1NuVGKMXHgLQnZ5uYt9max7ulUrsu_2iP/view?usp=sharing">
        <code>2565_1_Q1_02</code>
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
# File Name : 2565_1_Q1_02.py
# Problem   : Multiplexer
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------


# Returns the minimum positive integer from a, b, c
def f1(a, b, c):
    positives = []
    if a > 0:
        positives += [a]
    if b > 0:
        positives += [b]
    if c > 0:
        positives += [c]
    return min(positives)


# Returns the maximum negative integer from a, b, c
def f2(a, b, c):
    negatives = []
    if a < 0:
        negatives += [a]
    if b < 0:
        negatives += [b]
    if c < 0:
        negatives += [c]
    return max(negatives)


# Returns the first digit of the absolute sum of a, b, c
def f3(a, b, c):
    sums = abs(a + b + c)
    return str(sums)[0]


# Returns the last digit of the absolute sum of a, b, c
def f4(a, b, c):
    sums = abs(a + b + c)
    return str(sums)[-1]


# Main function to read input and call the appropriate function based on s1 and s2
def main():
    s1, s2, a, b, c = [int(e) for e in input().split()]
    if [s1, s2] == [0, 0]:
        print(f1(a, b, c))
    elif [s1, s2] == [0, 1]:
        print(f2(a, b, c))
    elif [s1, s2] == [1, 0]:
        print(f3(a, b, c))
    elif [s1, s2] == [1, 1]:
        print(f4(a, b, c))
    else:
        print("Error")


# Execute a input string as code
exec(input().strip())
```
