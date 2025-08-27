# --------------------------------------------------
# File Name : 03_If_JTP-02.py
# Problem   : Chinese Zodiac
# Author    : Worralop Srichainont
# Date      : 2025-08-14
# --------------------------------------------------

# Initialize the zodiac names
ZODIAC_NAMES = [
    "Monkey",
    "Rooster",
    "Dog",
    "Pig",
    "Rat",
    "Ox",
    "Tiger",
    "Rabbit",
    "Dragon",
    "Snake",
    "Horse",
    "Goat",
]

# Input month and year
month, year = [int(num) for num in input().split()]

# Shifting date backwards for one month
month -= 1
if month == 0:
    month = 12
    year -= 1

# Output the zodiac sign for the given date
print(ZODIAC_NAMES[year % 12])
