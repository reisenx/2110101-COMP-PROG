<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Scrabble ★★ (
      <a href="https://drive.google.com/file/d/1X6OZDtOLyN39IAgno2ZU1lD7gL25xOpo/view?usp=sharing">
        <code>2565_1_Q2_01</code>
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
# File Name : 2565_1_Q2_01.py
# Problem   : Scrabble
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

LETTER_POINT = [
    ["AEIOULNRST", 1],
    ["DG", 2],
    ["BCMP", 3],
    ["FHVWY", 4],
    ["K", 5],
    ["JX", 8],
    ["QZ", 10],
]


# Calculate the score of each letter in Scrabble
def get_letter_point(letter):
    for group, points in LETTER_POINT:
        if letter in group:
            return points
    return 0


# Calculate the total score of a word based on its letters
def word_point(word):
    total_point = 0
    for letter in word:
        total_point += get_letter_point(letter)
    return total_point


# Read input words and calculate their scores
word_points = []
for word in input().split():
    points = word_point(word)
    word_points.append([-points, word])

# Sort the words by their scores in descending order
# if scores are equal, sort alphabetically
word_points.sort()
# Output the words with their scores
for points, word in word_points:
    print(word, -points)
```
