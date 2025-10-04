<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Card Order ★★ (
      <a href="https://drive.google.com/file/d/1NdETVe680VmxhyiD0-egVZmvii14B4il/view?usp=sharing">
        <code>2567_1_Q3_B2-S</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**Solution 1**](#solution-1)
-   [**Solution 2**](#solution-2)

---

<div align="center">
  <h2>เฉลยอย่างละเอียดจะตามมาทีหลัง</h2>
</div>

---

# Solution 1

```python
# --------------------------------------------------
# File Name : 2567_1_Q3_B2-S-sol1.py
# Problem   : Card Sorting
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Initialize lists for each suit
VALUE_EX = {"J": 11, "Q": 12, "K": 13, "A": 14}
SUIT = {"S": 0, "C": 1, "D": 2, "H": 3}

# Input cards as a list of strings
cards_str = input().strip("| ").split("|")

# Initialize a list to hold card sublist
cards = []

# Iterate through each card string
for card in cards_str:
    # Extract value from the card string
    value = 0
    if card[:-1] in VALUE_EX:
        value = VALUE_EX[card[:-1]]
    else:
        value = int(card[:-1])

    # Extract suit from the card string
    suit = SUIT[card[-1]]

    # Append the card sublist for sorting
    cards.append([suit, value, card])

# Sort the cards based on suit and value in ascending order
cards.sort()

# Construct the output string
output = "|"
for _, _, card in cards:
    output += f"{card}|"

# Output the output string
print(output)
```

# Solution 2

```python
# --------------------------------------------------
# File Name : 2567_1_Q3_B2-S-sol2.py
# Problem   : Card Sorting
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Initialize lists for each suit
VALUE_EX = {"J": 11, "Q": 12, "K": 13, "A": 14}
SUIT = {"S": 0, "C": 1, "D": 2, "H": 3}


# Create a class to represent a card
class Card:
    # Initialize the card with its name, value and suit
    def __init__(self, card):
        # Initialize card name
        self.name = card

        # Initialize card suit by converting to integer
        self.suit = SUIT[card[-1]]

        # Initialize card value by converting to integer
        if card[:-1] in VALUE_EX:
            self.value = VALUE_EX[card[:-1]]
            return
        self.value = int(card[:-1])

    # Convert card to string representation
    def __str__(self):
        return self.name

    # Define less than operator for sorting by comparing suit and value
    def __lt__(self, rhs):
        return (self.suit, self.value) < (rhs.suit, rhs.value)


# Create a list of Card objects from the input and sort them in ascending order
card_objects = [Card(card) for card in input().strip("| ").split("|")]
card_objects.sort()

# Convert sorted Card objects back to string representation
cards = [str(card) for card in card_objects]

# Output the sorted cards with '|' at the start and end
print(f"|{'|'.join(cards)}|")
```
