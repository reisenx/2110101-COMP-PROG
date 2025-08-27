# --------------------------------------------------
# File Name : 02_StrList_JTP.py
# Problem   : Name and Birthday
# Author    : Worralop Srichainont
# Date      : 2025-08-14
# --------------------------------------------------

# Extract name and birthday from the input
raw_name, raw_date = input().strip().split(":")
surname, name = raw_name.split(",")
day, month, year = raw_date.split("/")

# Output the formatted string
print(f"{name} {surname}: {month} {day}, {year}")
