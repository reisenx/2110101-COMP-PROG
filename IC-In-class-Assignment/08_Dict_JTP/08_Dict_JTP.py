# --------------------------------------------------
# File Name : 08_Dict_JTP.py
# Problem   : Pizza Calories
# Author    : Worralop Srichainont
# Date      : 2025-08-14
# --------------------------------------------------

# Initialize calories for each pizza
PIZZA_CALORIES = {
    "PZ871": 265.25,
    "PZ953": 246.50,
    "Z1983": 256.50,
    "Z2853": 272.50,
    "LC673": 309.25,
}

# Initialize dictionary to store total calories of each customer
customer_calories = {}

# Input
n = int(input())
for _ in range(n):
    # Input customer order
    raw_data = input().strip().split(",")

    # Extract customer ID from the input
    customer_id = raw_data[0].strip()

    # Initialize customer's total calories if not already done
    if customer_id not in customer_calories:
        customer_calories[customer_id] = 0.0

    # Calculate total calories for the current order
    for i in range(1, len(raw_data), 2):
        # Extract pizza ID and amount from the input
        pizza_id = raw_data[i].strip()
        amount = int(raw_data[i + 1].strip())

        # Update customer's total calories
        customer_calories[customer_id] += PIZZA_CALORIES[pizza_id] * amount

# Output each customer's total calories sorted by customer ID
for customer_id, calories in sorted(customer_calories.items()):
    print(f"{customer_id} -> {round(calories, 2)}")
