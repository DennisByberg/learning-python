# Nested Loops

## What are Nested Loops?

A **loop inside another loop**. The inner loop executes **completely** for each iteration of the outer loop.

```python
for x in range(3):
    for y in range(2):
        print(f"({x}, {y})")

# Output:
# (0, 0)
# (0, 1)
# (1, 0)
# (1, 1)
# (2, 0)
# (2, 1)
```

## How It Works

1. Outer loop runs **once**
2. Inner loop runs **completely**
3. Outer loop moves to next iteration
4. Repeat

```python
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# Output:
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)
# ... and so on
```

## Practical Example - Multiplication Table

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Empty line after each table

# Output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
#
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# ...
```

## Practical Example - Grid Pattern

```python
for row in range(3):
    for col in range(5):
        print("*", end=" ")
    print()  # New line after each row

# Output:
# * * * * *
# * * * * *
# * * * * *
```

## Key Points

- **Nested loops** - loop inside a loop
- Inner loop executes **completely** for each outer iteration
- Useful for **2D data**, **grids**, **combinations**
- Can impact **performance** with large ranges
