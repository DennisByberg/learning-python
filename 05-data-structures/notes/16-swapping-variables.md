# Swapping Variables

## What is Swapping Variables?

Swapping variables means **exchanging the values** of two variables.

## The Python Way

```python
x = 10
y = 11

x, y = y, x

print(x)  # 11
print(y)  # 10
```

## How It Works

Uses **tuple unpacking** behind the scenes:

```python
x, y = y, x  # Same as: x, y = (y, x)
```

## Traditional Way (Other Languages)

```python
# Requires temp variable
temp = x
x = y
y = temp
```

## Multiple Variables

```python
a, b, c = 1, 2, 3
a, b, c = c, a, b  # Swap all at once
print(a, b, c)  # 3 1 2
```

## Key Points

- **`x, y = y, x`** - Pythonic way to swap
- Uses **tuple unpacking**
- **No temp variable** needed
- Works with **multiple variables**
