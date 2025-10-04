<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Euro 2024 ★★ (
      <a href="https://drive.google.com/file/d/1cBzc4kXgbFXzY45q16TeEZBRyL9_7gH3/view?usp=sharing">
        <code>2566_3_Q2_01</code>
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
# File Name : 2566_3_Q2_01.py
# Problem   : Euro 2024
# Author    : Worralop Srichainont
# Date      : 2025-07-15
# --------------------------------------------------


# Check if the match result of the guessed score is the same as the actual score.
# Both teams must have the same win/loss/draw status.
def is_match_result_same(exact, guess):
    return (
        ((exact[0] > exact[1]) and (guess[0] > guess[1]))
        or ((exact[0] < exact[1]) and (guess[0] < guess[1]))
        or ((exact[0] == exact[1]) and (guess[0] == guess[1]))
    )


# Compare the exact match scores with the guessed scores and return points.
# 3 points for exact match, 1 point for correct score of one team,
# and 0 points for no correct scores.
def get_match_scores(exact, guess):
    if exact == guess:
        return 3
    elif (exact[0] == guess[0]) or (exact[1] == guess[1]):
        return 1
    return 0


# Get the exact scores from the input.
exact_scores = []
while True:
    # Read input data until "-1" is entered.
    data = input().strip().split()
    if data == ["-1"]:
        break
    # Extract the scores from the input and store them in a list.
    score = data[1].split(":")
    exact_scores += [[int(score[0]), int(score[1])]]

# Get the guessed scores from the input.
guess_scores = []
for _ in range(len(exact_scores)):
    # Extract the scores from the input and store them in a list.
    score = input().strip().split(":")
    guess_scores += [[int(score[0]), int(score[1])]]

# Initialize total points to 0
total_points = 0
# Compare each exact score with the guessed score and calculate total points.
for i in range(len(exact_scores)):
    # Check if the match result is the same
    if is_match_result_same(exact_scores[i], guess_scores[i]):
        # If the match result is the same, compare scores and add points.
        total_points += get_match_scores(exact_scores[i], guess_scores[i])
# Output the total points.
print(total_points)
```
