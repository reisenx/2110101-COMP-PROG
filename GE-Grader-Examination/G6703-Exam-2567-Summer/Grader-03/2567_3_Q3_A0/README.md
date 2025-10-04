<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Total Card Value ★ (
        <code>2567_3_Q3_A0</code>
    )
  </h1>
</div>

# Contents

-   [**Problem**](#problem)
-   [**Solution**](#solution)

---

# Problem

จงอธิบายกระบวนการทำงานของโปรแกรมดังกล่าว

```python
# --------------------------------------------------
# File Name : 2567_3_Q3_A0.py
# Problem   : Total Card Value
# Author    : Worralop Srichainont
# Date      : 2025-07-26
# --------------------------------------------------

# --------------------------------------------------
# THIS IS A GRADER PROBLEM, NOT A SOLUTION.
# length_limit: 300
# nonIO_step_limit: 4
# --------------------------------------------------

C = input().split()
total = 0
for c in C:
    if c == "2":
        p = 2
    elif c == "3":
        p = 3
    elif c == "4":
        p = 4
    elif c == "5":
        p = 5
    elif c == "6":
        p = 6
    elif c == "7":
        p = 7
    elif c == "8":
        p = 8
    elif c == "9":
        p = 9
    elif c in "JQK":
        p = 10
    elif c == "A":
        p = 1
    total += p
print(total)
```

---

# Solution

-   นำเข้า (`input`) ข้อมูลเป็นข้อความประกอบด้วยไพ่หลายใบ คั่นด้วยช่องว่าง
-   ใช้คำสั่ง `.split()` เพื่อแบ่งข้อความด้วยช่องว่าง ได้ลิสต์ของไพ่

```python
C = input().split()
```

-   กำหนดให้ `total` หมายถึง แต้มรวมของไพ่ทั้งหมดในลิสต์ `C`
-   ลูปไพ่แต่ละใบบนลิสต์ `C` และแปลงสัญลักษณ์บนไพ่แต่ละใบให้เป็นแต้ม
    -   ไพ่ `A` มีแต้มเท่ากับ `1`
    -   ไพ่ `J`, `Q` และ `K` มีแต้มเท่ากับ `10`
    -   ไพ่ที่เป็นตัวเลขอยู่แล้ว มีแต้มตามตัวเลขบนไพ่
-   ในแต่ละลูป ให้เพิ่มแต้มลงไปใน `total` ด้วย

```python
total = 0
for c in C:
    if c == "2":
        p = 2
    elif c == "3":
        p = 3
    elif c == "4":
        p = 4
    elif c == "5":
        p = 5
    elif c == "6":
        p = 6
    elif c == "7":
        p = 7
    elif c == "8":
        p = 8
    elif c == "9":
        p = 9
    elif c in "JQK":
        p = 10
    elif c == "A":
        p = 1
    total += p
```

แสดงผลแต้มรวมของไพ่ทั้งหมดบนหน้าจอ

```python
print(total)
```
