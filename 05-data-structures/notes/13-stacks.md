# Stacks

## What is a Stack?

A stack is a **Last In, First Out (LIFO)** data structure where items are added and removed from the **same end**.

Think of it like a **stack of plates** - you add plates on top and remove them from the top.

## Stack Operations

### LIFO Principle

```python
stack = []

# Push items onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)  # [1, 2, 3]

# Pop items from the stack
last = stack.pop()
print(last)    # 3 (last item added)
print(stack)   # [1, 2]
```

## Implementing a Stack

Python lists work perfectly as stacks using **`append()`** and **`pop()`**.

```python
stack = []

# Push operation - add to top
stack.append("Apple")
stack.append("Banana")
stack.append("Cherry")

print(stack)  # ["Apple", "Banana", "Cherry"]

# Pop operation - remove from top
top_item = stack.pop()
print(top_item)  # "Cherry"
print(stack)     # ["Apple", "Banana"]
```

## Common Stack Use Cases

### 1. Browser History

```python
browsing_session = []

# Visit pages
browsing_session.append("google.com")
browsing_session.append("github.com")
browsing_session.append("stackoverflow.com")

# Go back
last_page = browsing_session.pop()
print(f"Left: {last_page}")  # "stackoverflow.com"

# Current page
if browsing_session:
    print(f"Current: {browsing_session[-1]}")  # "github.com"
```

### 2. Undo Functionality

```python
actions = []

# Perform actions
actions.append("Type 'Hello'")
actions.append("Type 'World'")
actions.append("Delete 'World'")

print(actions)  # ["Type 'Hello'", "Type 'World'", "Delete 'World'"]

# Undo last action
last_action = actions.pop()
print(f"Undoing: {last_action}")  # "Undoing: Delete 'World'"
```

## Checking Stack State

### Check if Empty

```python
stack = []

if not stack:
    print("Stack is empty")

stack.append(1)

if stack:
    print("Stack has items")
```

### Peek at Top (without removing)

```python
stack = [1, 2, 3, 4, 5]

# Look at top item without removing it
if stack:
    top = stack[-1]
    print(f"Top item: {top}")  # 5
    print(stack)               # [1, 2, 3, 4, 5] (unchanged)
```

## Stack Methods

| Operation | Method                           | Description                      |
| --------- | -------------------------------- | -------------------------------- |
| Push      | `stack.append(item)`             | Add item to top                  |
| Pop       | `stack.pop()`                    | Remove and return top item       |
| Peek      | `stack[-1]`                      | View top item (without removing) |
| Is Empty  | `not stack` or `len(stack) == 0` | Check if stack is empty          |
| Size      | `len(stack)`                     | Get number of items              |

## Complete Stack Example

```python
# Initialize empty stack
stack = []

# Push items
stack.append(10)
stack.append(20)
stack.append(30)

print(f"Stack: {stack}")           # [10, 20, 30]
print(f"Size: {len(stack)}")       # 3
print(f"Top item: {stack[-1]}")    # 30

# Pop item
removed = stack.pop()
print(f"Removed: {removed}")       # 30
print(f"Stack: {stack}")           # [10, 20]

# Check if empty
if not stack:
    print("Stack is empty")
else:
    print("Stack has items")       # This will print
```

## Error Handling

```python
stack = []

# Trying to pop from empty stack causes IndexError
try:
    item = stack.pop()
except IndexError:
    print("Cannot pop from empty stack")

# Safe pop
if stack:
    item = stack.pop()
else:
    print("Stack is empty")
```

## Key Points

- **LIFO** - Last In, First Out principle
- **`append()`** - push items onto stack (add to top)
- **`pop()`** - remove and return top item
- **`[-1]`** - peek at top item without removing
- **`not stack`** - check if stack is empty
- Lists in Python work perfectly as stacks
- Common uses: browser history, undo/redo, function calls
- Always check if stack is empty before popping
- `pop()` on empty stack raises **IndexError**
