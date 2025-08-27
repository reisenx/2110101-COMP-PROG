# --------------------------------------------------
# File Name : 07_StrFile_JTP.py
# Problem   : Capitalization
# Author    : Worralop Srichainont
# Date      : 2025-08-14
# --------------------------------------------------

# Input a list of words
raw_words = input().strip().split(",")

# Initialize a list to store formatted words
words = []

# Format each word, and store it to a list
for raw_word in raw_words:
    word = raw_word.strip().lower()
    word = f"{word[0].upper()}{word[1:]}"
    words.append(word)

# Output
print(" ".join(words))
