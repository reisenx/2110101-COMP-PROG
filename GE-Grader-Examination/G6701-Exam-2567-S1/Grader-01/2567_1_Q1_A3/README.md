<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Image Rotation ★★ (
      <a href="https://drive.google.com/file/d/1w2NXIPMJdgbLTamYX4en2fHmGKXnAClv/view?usp=sharing">
        <code>2567_1_Q1_A3</code>
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
# File Name : 2567_1_Q1_A3.py
# Problem   : Image Rotation
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input number of rows and the image
rows = int(input())
img = [input().strip() for _ in range(rows)]

# Find the number of columns
cols = len(img[0])

# Initialize the modified image
modified_img = []

# Input command to modify the image
cmd = input().strip()

# Rotate the image by 90 degrees clockwise
if cmd == "rot90":
    for c in range(cols):
        line = ""
        for r in range(rows - 1, -1, -1):
            line += img[r][c]
        modified_img.append(line)

# Rotate the image by 180 degrees
elif cmd == "rot180":
    for r in range(rows - 1, -1, -1):
        modified_img.append(img[r][::-1])

# Output the modified image
for line in modified_img:
    print(line)
```
