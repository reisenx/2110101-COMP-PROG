<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Gradsons ★★☆ (
      <a href="https://drive.google.com/file/d/1DckIjdZe0aP7xbSN2p3_BLqjfuZG5_QB/view?usp=sharing">
        <code>2567_2_Q3_C2</code>
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
# File Name : 2567_2_Q3_C2-sol1.py
# Problem   : Grandsons
# Author    : Worralop Srichainont
# Date      : 2025-07-30
# --------------------------------------------------

# Initialize a dictionary to store the children of each person
children = {}

# Input relationships in the family and build the dictionary
n = int(input())
for _ in range(n):
    # Input relationships
    parent, child = input().strip().split()

    # Update the dictionary with the parent-child relationship
    if parent not in children:
        children[parent] = set()
    if child not in children:
        children[child] = set()
    children[parent].add(child)

# Input the names of people to query
queries = input().strip().split()

# Output the number of grandchildren for each queried person
for person in queries:
    # If the person exists in the dictionary, count their grandchildren
    if person in children:
        # Initialize a counter for grandchildren
        total_grandchildren = 0

        # Count the children of each child of the person
        for child in children[person]:
            if child in children:
                total_grandchildren += len(children[child])

        # Output the total number of grandchildren
        print(total_grandchildren)

    # If the person does not exist in the dictionary, output 0
    else:
        print(0)
```

---

# Solution 2

```python
# --------------------------------------------------
# File Name : 2567_2_Q3_C2-sol2.py
# Problem   : Grandson
# Author    : Worralop Srichainont
# Date      : 2025-07-30
# --------------------------------------------------


# Define the Node class to represent each node in the tree
class Node:
    # Initialize the node with a name and its children
    def __init__(self, name):
        self.name = name
        self.children = set()

    # Add a child node to the current node
    def add_child(self, child):
        child.parent = self
        self.children.add(child)

    # Count the number of grandchildren for the current node
    def count_grandchildren(self):
        total_grandchildren = 0
        for child in self.children:
            total_grandchildren += len(child.children)
        return total_grandchildren


# Main function
def main():
    # Initialize a dictionary to store nodes
    nodes = {}

    # Input the number of relationships and build the tree
    n = int(input())
    for _ in range(n):
        # Extract parent node and child node from input
        parent, child = input().strip().split()
        # Initialize parent and child nodes if they do not exist
        if parent not in nodes:
            nodes[parent] = Node(parent)
        if child not in nodes:
            nodes[child] = Node(child)
        # Add the child node to the parent node
        nodes[parent].add_child(nodes[child])

    # Input the names of nodes to query
    query_nodes = input().strip().split()
    # Output the number of grandchildren for each queried node
    for node in query_nodes:
        if node in nodes:
            print(nodes[node].count_grandchildren())
        else:
            print(0)


# Run the main function
main()
```
