# Queues

## What is a Queue?

A queue is a **First In, First Out (FIFO)** data structure where items are added at one end and removed from the other end.

Think of it like a **line at a store** - the first person in line is the first to be served.

## Queue Operations

### FIFO Principle

```python
from collections import deque

queue = deque([])

# Add items to the queue
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)  # deque([1, 2, 3])

# Remove items from the queue
first = queue.popleft()
print(first)   # 1 (first item added)
print(queue)   # deque([2, 3])
```

## Why Use deque?

Regular lists are **inefficient** for queues because removing from the beginning (`pop(0)`) is slow.

**`deque`** (double-ended queue) from `collections` is **optimized** for both ends.

```python
from collections import deque

# Good - Using deque (fast)
queue = deque([])
queue.append(1)        # Add to end - O(1)
queue.popleft()        # Remove from front - O(1)

# Bad - Using list (slow)
queue = []
queue.append(1)        # Add to end - O(1)
queue.pop(0)           # Remove from front - O(n) SLOW!
```

## Implementing a Queue

```python
from collections import deque

queue = deque([])

# Enqueue - add to back
queue.append("Alice")
queue.append("Bob")
queue.append("Charlie")

print(queue)  # deque(["Alice", "Bob", "Charlie"])

# Dequeue - remove from front
first_person = queue.popleft()
print(first_person)  # "Alice"
print(queue)         # deque(["Bob", "Charlie"])
```

## Common Queue Use Cases

### 1. Customer Service Line

```python
from collections import deque

waiting_line = deque([])

# Customers arrive
waiting_line.append("Customer 1")
waiting_line.append("Customer 2")
waiting_line.append("Customer 3")

print(f"Waiting: {waiting_line}")

# Serve customers
served = waiting_line.popleft()
print(f"Now serving: {served}")  # "Customer 1"
print(f"Remaining: {waiting_line}")
```

### 2. Print Queue

```python
from collections import deque

print_queue = deque([])

# Add documents
print_queue.append("Document1.pdf")
print_queue.append("Document2.pdf")
print_queue.append("Document3.pdf")

# Process documents in order
while print_queue:
    doc = print_queue.popleft()
    print(f"Printing: {doc}")
```

### 3. Task Scheduler

```python
from collections import deque

tasks = deque([])

# Schedule tasks
tasks.append("Send email")
tasks.append("Update database")
tasks.append("Generate report")

# Execute tasks in order
while tasks:
    task = tasks.popleft()
    print(f"Executing: {task}")
```

## Checking Queue State

### Check if Empty

```python
from collections import deque

queue = deque([])

if not queue:
    print("Queue is empty")

queue.append(1)

if queue:
    print("Queue has items")
```

### Peek at Front (without removing)

```python
from collections import deque

queue = deque([1, 2, 3, 4, 5])

# Look at front item without removing it
if queue:
    front = queue[0]
    print(f"Front item: {front}")  # 1
    print(queue)                    # deque([1, 2, 3, 4, 5])
```

## Queue Methods

| Operation  | Method                           | Description                        |
| ---------- | -------------------------------- | ---------------------------------- |
| Enqueue    | `queue.append(item)`             | Add item to back                   |
| Dequeue    | `queue.popleft()`                | Remove and return front item       |
| Peek Front | `queue[0]`                       | View front item (without removing) |
| Peek Back  | `queue[-1]`                      | View back item (without removing)  |
| Is Empty   | `not queue` or `len(queue) == 0` | Check if queue is empty            |
| Size       | `len(queue)`                     | Get number of items                |

## Complete Queue Example

```python
from collections import deque

# Initialize empty queue
queue = deque([])

# Enqueue items
queue.append(10)
queue.append(20)
queue.append(30)

print(f"Queue: {queue}")              # deque([10, 20, 30])
print(f"Size: {len(queue)}")          # 3
print(f"Front item: {queue[0]}")      # 10
print(f"Back item: {queue[-1]}")      # 30

# Dequeue item
removed = queue.popleft()
print(f"Removed: {removed}")          # 10
print(f"Queue: {queue}")              # deque([20, 30])

# Check if empty
if not queue:
    print("Queue is empty")
else:
    print("Queue has items")          # This will print
```

## Error Handling

```python
from collections import deque

queue = deque([])

# Trying to popleft from empty queue causes IndexError
try:
    item = queue.popleft()
except IndexError:
    print("Cannot dequeue from empty queue")

# Safe dequeue
if queue:
    item = queue.popleft()
else:
    print("Queue is empty")
```

## Queue vs Stack

| Feature        | Queue                      | Stack                     |
| -------------- | -------------------------- | ------------------------- |
| Principle      | FIFO (First In, First Out) | LIFO (Last In, First Out) |
| Add            | `append()` (back)          | `append()` (top)          |
| Remove         | `popleft()` (front)        | `pop()` (top)             |
| Data Structure | `deque`                    | `list`                    |
| Example        | Line at store              | Stack of plates           |

## Key Points

- **FIFO** - First In, First Out principle
- **`from collections import deque`** - import deque
- **`deque([])`** - create empty queue
- **`append()`** - enqueue items (add to back)
- **`popleft()`** - dequeue items (remove from front)
- **`[0]`** - peek at front item without removing
- **`not queue`** - check if queue is empty
- **deque is faster** than list for queue operations
- Common uses: task scheduling, breadth-first search, print queues
- Always check if queue is empty before dequeuing
- `popleft()` on empty queue raises **IndexError**
