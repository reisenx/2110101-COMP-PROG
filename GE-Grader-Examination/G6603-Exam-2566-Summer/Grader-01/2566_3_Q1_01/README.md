<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Longest Repeating Characters ★☆ (
      <a href="https://drive.google.com/file/d/1EzqYAfhvcaWUq-5EzXJwyZBHy3k4C9CK/view?usp=sharing">
        <code>2566_3_Q1_01</code>
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
# File Name : 2566_3_Q1_01.py
# Problem   : Longest Repeated Characters
# Author    : Worralop Srichainont
# Date      : 2025-07-15
# --------------------------------------------------

# Input text
text = input().strip()

# Initialize counter
max_char = text[0]
char = text[0]

max_count = 1
count = 1

# Iterate through the text
for i in range(1, len(text)):
    if text[i] == char:
        count += 1
    else:
        if count > max_count:
            max_count = count
            max_char = char
        char = text[i]
        count = 1

# Check the last character count
if count > max_count:
    max_count = count
    max_char = char

# Output the maximum character repeated and its count
print(max_char, max_count)
```
