<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Match ★★☆ (
      <a href="https://drive.google.com/file/d/14nVgkqWfDCmAo63yftuhC75UoOSFs9Xi/view?usp=sharing">
        <code>2565_1_Q2_02</code>
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
# File Name : 2565_1_Q2_02.py
# Problem   : Match
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------


# Check if a word matches a given pattern
def is_pattern_match(word, pattern):
    # Check if the lengths of the word and pattern are the same
    if len(word) != len(pattern):
        return False

    # Check each character in the word against the pattern
    # Skip characters in the pattern that are '?'
    for i in range(len(word)):
        if pattern[i] != "?" and pattern[i] != word[i]:
            return False
    return True


# Check if all letters in ? position are in the excluded characters
def has_excluded_char(word, pattern, excluded_chars):
    for i in range(len(word)):
        if pattern[i] == "?" and word[i] in excluded_chars:
            return True
    return False


# Check if all letters in ? position are in the included characters
def has_all_included_chars(word, pattern, included_chars):
    # Collect letters from the word that are in ? positions
    filled_letters = []
    for i in range(len(word)):
        if pattern[i] == "?":
            filled_letters.append(word[i])

    # Check if all included characters are in the filled letters
    for char in included_chars:
        if char not in filled_letters:
            return False
        # Remove the checked character
        filled_letters.remove(char)
    return True


def match(word, pattern, included_chars, excluded_chars):
    # Check if the word matches the pattern
    if not is_pattern_match(word, pattern):
        return False

    # Check if the word contains any excluded characters
    if has_excluded_char(word, pattern, excluded_chars):
        return False

    return has_all_included_chars(word, pattern, included_chars)


# Execute a input string as code
exec(input().strip())
```
