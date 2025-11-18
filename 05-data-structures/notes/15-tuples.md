# Tuples

## What is a Tuple?

A tuple is an **ordered, immutable collection** - like a **read-only list**.

## Creating Tuples

```python
# Using parentheses
point = (1, 2)
coordinates = (10, 20, 30)

# Without parentheses (tuple packing)
person = "Alice", 25, "Engineer"

# Single item tuple (comma required!)
single = (1,)
not_tuple = (1)  # This is just an integer

# Empty tuple
empty = ()
```

## Immutability

```python
point = (1, 2)
point[0] = 10  # TypeError: 'tuple' object does not support item assignment
```

## Accessing Items

```python
point = (1, 2, 3)
print(point[0])   # 1
print(point[-1])  # 3
```

## Tuple Unpacking

```python
point = (1, 2)
x, y = point

# Swapping values
a, b = b, a
```

## Tuple Concatenation

```python
point1 = (1, 2)
point2 = (3, 4)
combined = point1 + point2  # (1, 2, 3, 4)
```

## Tuple Methods

Only **2 methods** (because immutable):

```python
numbers = (1, 2, 2, 3, 2, 4)
numbers.count(2)  # 3

letters = ("a", "b", "c", "d")
letters.index("c")  # 2
```

## Common Use Cases

```python
# Coordinates
point = (10, 20)
x, y = point

# RGB colors
red = (255, 0, 0)

# Function returns
def min_max(numbers):
    return (min(numbers), max(numbers))

minimum, maximum = min_max([1, 2, 3, 4, 5])
```

## Tuple vs List

| Feature  | Tuple       | List        |
| -------- | ----------- | ----------- |
| Mutable  | No          | Yes         |
| Speed    | Faster      | Slower      |
| Methods  | 2           | Many        |
| Dict key | Yes         | No          |
| Syntax   | `(1, 2, 3)` | `[1, 2, 3]` |

## Key Points

- **Immutable** - cannot be changed after creation
- **Comma** makes it a tuple, not parentheses
- Single item needs **trailing comma**: `(1,)`
- Can be used as **dictionary keys**
- **Unpacking** for easy variable assignment
- Only **2 methods**: `count()` and `index()`
- Use for **fixed data** that shouldn't change
- Common uses: coordinates, RGB values, function returns
