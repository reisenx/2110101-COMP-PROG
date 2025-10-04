<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    The Python ★★★☆ (
      <a href="https://drive.google.com/file/d/1QRbJQGZLhat6SViEl5cG1OF3q1H2LlX7/view?usp=sharing">
        <code>2567_1_Q3_C2</code>
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
# File Name : 2567_1_Q3_C2-sol1.py
# Problem   : The Python
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Initialize sets to store all employees and their bosses
all_employees = set()
boss_of = {}

# Initialize a dictionary to store sales values for each employee
sales = {}

# Input the subordinate and their boss along with the sales value
n = int(input())
for _ in range(n):
    # Extract subordinate, boss, and sales value from input
    sub, boss, sale = input().strip().split(",")

    # Add the subordinate and boss to the set of all employees
    all_employees.add(sub)
    all_employees.add(boss)

    # Add the boss to subordinate's boss mapping
    boss_of[sub] = boss
    # Add the sales value for the subordinate
    sales[sub] = int(sale)

    # Initialize the sales value for the boss if not already present
    if boss not in sales:
        sales[boss] = 0

# Add subordinates sales to their big boss
for sub, boss in boss_of.items():
    # Get the sales value of the subordinate
    sale = sales[sub]

    # Traverse up the hierarchy to find the big boss of the subordinate
    current_boss = boss
    while current_boss in boss_of:
        current_boss = boss_of[current_boss]

    # Add the subordinate's sales to the big boss's sales
    sales[current_boss] += sale

# Initialize a list to store the big boss and their total sales
result = []

# Find all big bosses (those who are not subordinates of anyone)
big_bosses = all_employees - set(boss_of.keys())

# Store the total sales for each big boss
for boss in big_bosses:
    result.append((-sales[boss], boss))
result.sort()

# Output the total sales for each big boss sorted by sales value in descending order
for sale, boss in result:
    print(f"Boss {boss} {-sale}")
```

---

# Solution 2

```python
# --------------------------------------------------
# File Name : 2567_1_Q3_C2-sol2.py
# Problem   : The Python
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Initialize dictionaries to store nodes and their total values
nodes = {}
total_values = {}


# Define the Node class to represent each node in the tree
class Node:
    # Initialize the node with a name, children, parent, and value
    def __init__(self, name):
        self.name = name
        self.children = set()
        self.parent = None
        self.value = 0

    # Define the integer representation of the node
    def __int__(self):
        return self.value

    # Add a child node to the current node
    def add_child(self, child):
        child.parent = self
        self.children.add(child)

    # Add a parent node to the current node
    def add_parent(self, parent):
        self.parent = parent
        parent.add_child(self)

    # Add a value to the current node
    def add_value(self, value):
        self.value += value

    # Check if the node has any children
    def has_child(self):
        return len(self.children) > 0

    # Check if the node has a parent
    def has_parent(self):
        return self.parent is not None


# Build a tree from n edges
def build_tree(n):
    for _ in range(n):
        # Extract child node, parent node, and child node value from input
        child, parent, value = input().strip().split(",")
        # Initialize child and parent nodes if they do not exist
        if child not in nodes:
            nodes[child] = Node(child)
        if parent not in nodes:
            nodes[parent] = Node(parent)

        # Add the child node to the parent node and set the value
        nodes[child].add_parent(nodes[parent])
        nodes[child].add_value(int(value))

        # Add the child node to the parent's children set
        nodes[parent].add_child(nodes[child])


# Recursively calculate the total values for each node
def get_total_values(node):
    # Check if the total value for this node has already been calculated
    if node.name in total_values:
        return total_values[node.name]

    # Initialize the total value with the node's own value
    total_value = int(node)
    # Recursively add the total values of all child nodes
    for child in node.children:
        total_value += get_total_values(child)
    # Store the total value for this node
    total_values[node.name] = total_value
    # Return the total value
    return total_value


# Display the total values for all root nodes of trees
def display_root_total_values():
    # Find all root nodes and calculate their total values
    root_values = []
    for node in nodes.values():
        # Check if the node is a root (has no parent)
        if not node.has_parent():
            # Store the total value and name of the root node
            total_value = get_total_values(node)
            root_values.append((-total_value, node.name))

    # Output the root values by total value in descending order
    # and name in ascending order
    for total_value, name in sorted(root_values):
        print(f"Boss {name} {-total_value}")


# Main function to read input and build the tree
def main():
    # Build the tree based on the number of edges
    n = int(input())
    build_tree(n)
    # Display the total values for all root nodes
    display_root_total_values()


# Call the main function to execute the program
main()
```
