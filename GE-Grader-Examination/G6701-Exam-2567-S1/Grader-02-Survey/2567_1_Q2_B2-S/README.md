<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Bad Words ★★ (
      <a href="https://drive.google.com/file/d/1lgfgUbFPWHh2C0xvCvfsrskLhjylms1b/view?usp=sharing">
        <code>2567_1_Q2_B2-S</code>
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
# File Name : 2567_1_Q2_B2-S.py
# Problem   : Offensive Words
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------


# Function to hide words by alternating characters with asterisks
def hide_word(word):
    result = ""
    for i in range(len(word)):
        if i % 2 == 0:
            result += word[i]
        else:
            result += "*"
    return result


# Censor the text by replacing offensive word with their hidden versions
def censor_text(text, target):
    # Initialize the result with the original text and search index
    result = text
    search_idx = 0

    # Loop to find and replace all occurrences of the target word
    while True:

        # Find the next occurrence of the target word
        start_idx = result.lower().find(target.lower(), search_idx)
        end_idx = start_idx + len(target)

        # If no more occurrences are found, break the loop
        if start_idx == -1:
            break

        # Replace the target word with its vowel-hidden version
        before_target = result[:start_idx]
        censored_target = hide_word(result[start_idx:end_idx])
        after_target = result[end_idx:]

        result = before_target + censored_target + after_target

        # Update the search index to continue searching after the replaced word
        search_idx = end_idx

    # Return the censored text
    return result


# Input offensive word and text
offensive_word = input().strip()
text = input().strip()

# Output the censored text
print(censor_text(text, offensive_word))
```
