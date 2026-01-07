# Type Conversion

## What is Type Conversion?

Converting one data type to another. Also called **type casting**.

```python
x = input("x: ")  # Returns string
x = int(x)        # Convert to integer
```

## Conversion Functions

```python
# String to Number
x = int("10")           # 10 (integer)
y = float("3.14")       # 3.14 (float)

# Number to String
x = str(10)             # "10" (string)

# Boolean
x = bool(1)             # True
x = bool(0)             # False
x = bool("")            # False
```

## Input Conversion

```python
# Wrong - input() returns string
age = input("Age: ")
next_year = age + 1   # Error!

# Correct - convert to int
age = int(input("Age: "))
next_year = age + 1   # Works!
```

## Falsy Values

Values that convert to `False`:

```python
bool("")      # False - empty string
bool(0)       # False - zero
bool(None)    # False - None
```

## Key Points

- **`input()`** always returns a string
- **`int()`** converts to integer
- **`float()`** converts to float
- **`str()`** converts to string
- **`bool()`** converts to True/False
- **Falsy values**: `""`, `0`, `None`
