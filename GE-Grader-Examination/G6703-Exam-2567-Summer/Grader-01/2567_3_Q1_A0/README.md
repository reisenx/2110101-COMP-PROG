<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Get Min-Max Out of 6 ★ (
        <code>2567_3_Q1_A0</code>
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
# File Name : 2567_3_Q1_A0.py
# Problem   : Get Min-Max Out of 6
# Author    : Worralop Srichainont
# Date      : 2025-07-26
# --------------------------------------------------

# --------------------------------------------------
# THIS IS A GRADER PROBLEM, NOT A SOLUTION.
# length_limit: 300
# nonIO_step_limit: 4
# --------------------------------------------------

d1 = float(input())
d2 = float(input())
d3 = float(input())
d4 = float(input())
d5 = float(input())
d6 = float(input())

m1 = d1
m2 = d1

if d2 > m1:
    m1 = d2
if d3 > m1:
    m1 = d3
if d4 > m1:
    m1 = d4
if d5 > m1:
    m1 = d5
if d6 > m1:
    m1 = d6

if d2 < m2:
    m2 = d2
if d3 < m2:
    m2 = d3
if d4 < m2:
    m2 = d4
if d5 < m2:
    m2 = d5
if d6 < m2:
    m2 = d6

s = (d1 + d2 + d3 + d4 + d5 + d6) - m1 - m2
print(s)
```

---

# Solution

นำเข้า (`input`) ข้อมูลประเภทจำนวนจริง (`float`) จากผู้ใช้งานทั้งหมด 6 ครั้ง
แต่ละครั้งเก็บข้อมูลใส่ตัวแปร `d1`, `d2`, `d3`, `d4`, `d5` และ `d6` ตามลำดับ

```python
d1 = float(input())
d2 = float(input())
d3 = float(input())
d4 = float(input())
d5 = float(input())
d6 = float(input())
```

-   กำหนดให้ ตัวแปร `m1` หมายถึง ค่ามากที่สุด จากจำนวน ทั้งหมด 6 ตัว (`d1` ถึง
    `d6`) โดยมีค่าเริ่มต้นเท่ากับ `d1`
-   กำหนดให้ ตัวแปร `m2` หมายถึง ค่าน้อยที่สุด จากจำนวน ทั้งหมด 6 ตัว (`d1` ถึง
    `d6`) โดยมีค่าเริ่มต้นเท่ากับ `d1`

```python
m1 = d1
m2 = d1
```

-   พิจารณาว่าจำนวน `d2` มากกว่า ค่ามากที่สุด (`m1`) หรือไม่ หากมากกว่า
    ให้กำหนดค่ามากที่สุด (`m1`) ใหม่เป็น `d2` แทน
-   ทำซ้ำกระบวนการดังกล่าวไปเรื่อย ๆ โดยใช้จำนวน `d3`, `d4`, `d5` และ `d6` แทน
    จนครบทุกจำนวน

```python
if d2 > m1:
    m1 = d2
if d3 > m1:
    m1 = d3
if d4 > m1:
    m1 = d4
if d5 > m1:
    m1 = d5
if d6 > m1:
    m1 = d6
```

-   พิจารณาว่าจำนวน `d2` น้อยกว่า ค่าน้อยที่สุด (`m1`) หรือไม่ หากน้อยกว่า
    ให้กำหนดค่าน้อยที่สุด (`m1`) ใหม่เป็น `d2` แทน
-   ทำซ้ำกระบวนการดังกล่าวไปเรื่อย ๆ โดยใช้จำนวน `d3`, `d4`, `d5` และ `d6` แทน
    จนครบทุกจำนวน

```python
if d2 < m2:
    m2 = d2
if d3 < m2:
    m2 = d3
if d4 < m2:
    m2 = d4
if d5 < m2:
    m2 = d5
if d6 < m2:
    m2 = d6
```

-   กำหนดให้ `s` เป็นผลรวมของทุกจำนวน แต่หักลบค่าที่มากที่สุด (`m1`)
    และน้อยที่สุด (`m2`) ออกไป
-   คำนวณ และแสดงผลค่าของตัวแปร `s` ออกมาทางหน้าจอ

```python
s = (d1 + d2 + d3 + d4 + d5 + d6) - m1 - m2
print(s)
```
