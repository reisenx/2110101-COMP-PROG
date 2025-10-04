<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Grader Score ★★ (
      <a href="https://drive.google.com/file/d/1xH6vj4ppOagjY1tbTkR5sUHK3JA6TzU5/view?usp=sharing">
        <code>2567_1_Q3_A3</code>
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
# File Name : 2567_1_Q3_A3.py
# Problem   : Grader Score
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input grader scores for three quizzes
q1_scores = [int(score) for score in input().split()]
q2_scores = [int(score) for score in input().split()]
q3_scores = [int(score) for score in input().split()]

# Calculate the total number of quizzes
total_quizzes = max(len(q1_scores), len(q2_scores), len(q3_scores))

# Ensure all lists have the same length by padding with zeros
q1_scores += [0] * (total_quizzes - len(q1_scores))
q2_scores += [0] * (total_quizzes - len(q2_scores))
q3_scores += [0] * (total_quizzes - len(q3_scores))

# Initialize total score to 0
total_score = 0

# Calculate the total score by taking the maximum score from each quiz
for i in range(total_quizzes):
    total_score += max(q1_scores[i], q2_scores[i], q3_scores[i])

# Output the total score
print(total_score)
```
