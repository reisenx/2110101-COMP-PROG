<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Reality Show ★★ (
      <a href="https://drive.google.com/file/d/1Kmkh6j223BnjUQg9vZjQBdBVK_uOZTnC/view?usp=sharing">
        <code>2567_3_Q3_B1</code>
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
# File Name : 2567_3_Q3_B1.py
# Problem   : Reality Show
# Author    : Worralop Srichainont
# Date      : 2025-07-31
# --------------------------------------------------

# Constants for the number of top players to display
DISPLAY_LIMIT = 3

# Initialize a dictionary to store survival times of each player
survival_time = {}

# Input raw data
data = input().strip().split()

# Process the input data to calculate total survival time for each player
for i in range(0, len(data), 2):
    # Extract player name and time from the input data
    player = data[i]
    time = int(data[i + 1])

    # Update the survival time for the player
    if player not in survival_time:
        survival_time[player] = 0
    survival_time[player] += time

# Sort players by survival time in descending order and then by name in ascending order
sorted_survival_time = []
for player, time in survival_time.items():
    sorted_survival_time.append([-time, player])
sorted_survival_time.sort()

# Extract the top players based on survival time
top_player_names = []
for _, player in sorted_survival_time[:DISPLAY_LIMIT]:
    top_player_names.append(player)

# Output the names of the top players
print(" ".join(top_player_names))
```
