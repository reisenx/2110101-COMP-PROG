<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Coveyer Belt ★★ (
      <a href="https://drive.google.com/file/d/1rn2oJeFPBMSNHAICwYwckghCxUb7Coau/view?usp=sharing">
        <code>2567_3_Q3_A2</code>
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
# File Name : 2567_3_Q3_A2.py
# Problem   : Conveyor Belt
# Author    : Worralop Srichainont
# Date      : 2025-07-31
# --------------------------------------------------


# Initialize the conveyor belt string with items placed at the front
def init_conveyor_belt(conveyor_length, items):
    return items[::-1] + (conveyor_length * ".")


# Move the conveyor belt by shifting items to the right
def move_conveyor_belt(conveyor, time):
    return ("." * time) + conveyor[:-time]


# Display the conveyor belt in a rows x cols format
def display_conveyor_belt(conveyor, rows, cols):
    # Display only the last rows * cols characters of the conveyor belt
    conveyor_to_display = conveyor[-(rows * cols) :]

    # Output the conveyor belt in each row
    for i in range(rows):
        # Calculate the start and end indices for slicing from the conveyor string
        start_index = cols * i
        end_index = cols * (i + 1)

        # For even indexed rows, display normally
        if i % 2 == 0:
            print(conveyor_to_display[start_index:end_index])
        # For odd indexed rows, display in reverse order
        else:
            print(conveyor_to_display[start_index:end_index][::-1])


# Main function
def main():
    # Read the conveyor belt dimensions and time processed
    cols, rows, time = [int(num) for num in input().split()]
    # Read the items to be placed on the conveyor belt
    items = input().strip()

    # Calculate the total length of the conveyor belt
    conveyor_length = cols * rows

    # Initialize the conveyor belt string
    conveyor = init_conveyor_belt(conveyor_length, items)

    # Move the conveyor belt by the specified time
    conveyor = move_conveyor_belt(conveyor, time)

    # Output
    display_conveyor_belt(conveyor, rows, cols)


# Run the main function
main()
```
