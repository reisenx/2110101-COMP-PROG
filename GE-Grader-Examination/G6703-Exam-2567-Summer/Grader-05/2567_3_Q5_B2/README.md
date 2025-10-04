<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Weather Perception ★★☆ (
      <a href="https://drive.google.com/file/d/1TMVjvnJ1ltHH8S8_CrdAnlekX9SKm-QQ/view?usp=sharing">
        <code>2567_3_Q5_B2</code>
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
# File Name : 2567_3_Q5_B2.py
# Problem   : Weather Perception
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

# Constants for temperature perception
PERCEPTION_ORDER = ["comfortable", "cold", "hot", "extreme cold", "extreme hot"]
PERCEPTION_CRITERIA = [
    ["extreme hot", 35.0],
    ["hot", 25.0],
    ["comfortable", 15.0],
    ["cold", -10.0],
]


# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Function to determine the weather perception based on Celsius temperature
def get_perception(celsius):
    for perception, threshold in PERCEPTION_CRITERIA:
        if celsius > threshold:
            return perception
    return "extreme cold"


# Function to print countries ranked by their weather perception
def print_countries_ranked_by_perception(countries_info):
    # Initialize a dictionary to map perceptions to countries
    perception_to_countries = {}

    # Process each country's information
    for country, fahrenheit in countries_info:
        # Determine perception from the Fahrenheit temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        perception = get_perception(celsius)

        # Add the country to the corresponding perception in the dictionary
        if perception not in perception_to_countries:
            perception_to_countries[perception] = []
        perception_to_countries[perception].append(country)

    # Print the countries sorted by perception order
    for perception in PERCEPTION_ORDER:
        # Check if the perception exists in the dictionary
        if perception in perception_to_countries:
            # Sort the countries alphabetically and print them with their perception
            for country in sorted(perception_to_countries[perception]):
                print(country, perception)


# Run the input string as code until it ends with a semicolon
while cmd := input().strip():
    exec(cmd)
    if cmd[-1] == ";":
        break
```
