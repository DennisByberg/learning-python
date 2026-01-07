# For Loops

## What are For Loops?

**Iterate** over a sequence (range, list, string, etc.) and execute code for each item.

```python
for number in range(3):
    print(number)
# Output:
# 0
# 1
# 2
```

## The `range()` Function

Generates a sequence of numbers.

```python
# range(stop) - from 0 to stop (exclusive)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - from start to stop (exclusive)
for i in range(1, 5):
    print(i)  # 1, 2, 3, 4

# range(start, stop, step) - with step increment
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9
```

## Iterating Over Strings

```python
for char in "Python":
    print(char)
# Output:
# P
# y
# t
# h
# o
# n
```

## Iterating Over Lists

```python
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(name)
# Output:
# Alice
# Bob
# Charlie
```

## Practical Example

```python
# Your example - printing attempts with dots
for number in range(1, 10, 2):
    print("Attempt", number, (number + 1) * ".")

# Output:
# Attempt 1 ..
# Attempt 3 ....
# Attempt 5 ......
# Attempt 7 ........
# Attempt 9 ..........
```

## Key Points

- **For loops** iterate over sequences
- **`range(stop)`** - from 0 to stop (exclusive)
- **`range(start, stop)`** - from start to stop (exclusive)
- **`range(start, stop, step)`** - with custom increment
- Can iterate over **strings**, **lists**, and other iterables
- **String multiplication** - `"." * 3` → `"..."`
