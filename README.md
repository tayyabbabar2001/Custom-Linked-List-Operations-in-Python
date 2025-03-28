# Custom-Linked-List-Operations-in-Python
Implementation of a custom Linked List class without using Python's built-in list. Includes methods for insertion, deletion, search, size, duplicate removal, and node swapping. Demonstrates fundamental Linked List operations for DSA practice.

# Linked List Implementation in Python

This project implements a custom **Singly Linked List** in Python without using Python's built-in list datatype. The goal is to practice and demonstrate fundamental data structure concepts and manipulation of nodes.

---

## Features

This linked list supports the following operations:

### ✅ Basic Operations
- `add(item, position)`: Adds an item at the specified position in the linked list.
- `remove(item)`: Removes the first occurrence of an item by value.
- `remove(position)`: Removes the node at the specified position.
- `get(position)`: Returns the item present at the given position.
- `search(item)`: Searches for an item and returns its position, returns -1 if not found.
- `size()`: Returns the total number of elements in the linked list.

---

### ✅ Additional Functionalities
- `removeDuplicates()`: Removes duplicate values from the linked list, leaving only the first occurrence.
- `swapNodes(pos1, pos2)`: Swaps two nodes in the linked list using their positions.
- Full testing code included to demonstrate each method.

---

## Example Usage
```python
ll = LinkedList()
ll.add(10, 0)     # [10]
ll.add(20, 1)     # [10, 20]
ll.add(15, 1)     # [10, 15, 20]
ll.remove(15)     # [10, 20]
ll.add(20, 2)     # [10, 20, 20]
ll.removeDuplicates()  # [10, 20]
ll.swapNodes(0, 1) # [20, 10]
print(ll.size())   # 2
