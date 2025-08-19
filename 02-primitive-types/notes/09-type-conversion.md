# Type Conversion

## What is Type Conversion?

Converting one data type to another. Also called **type casting**.

```python
x = input("x: ")  # Returns string
x = int(x)        # Convert to integer
```

## Built-in Conversion Functions

### String to Number

```python
x = input("x: ")     # "10" (string)
x = int(x)           # 10 (integer)
y = float(x)         # 10.0 (float)
```

### Number to String

```python
x = 10
x = str(x)           # "10" (string)
```

### Boolean Conversion

```python
x = bool(1)          # True
x = bool(0)          # False
x = bool("")         # False
x = bool("Hello")    # True
```

## Common Conversions

### Input Conversion

```python
# Wrong - input() returns string
age = input("Age: ")
next_year = age + 1   # Error!

# Correct - convert to int
age = int(input("Age: "))
next_year = age + 1   # Works!
```

### One-line Conversion

```python
x = int(input("x: "))  # Convert directly
y = float(input("Price: "))
```

## Falsy Values

Values that convert to `False`:

```python
print(bool(""))      # False - empty string
print(bool(0))       # False - zero
print(bool(None))    # False - None
print(bool([]))      # False - empty list
```

## Key Points

- **`input()`** always returns a string
- **`int()`** converts to integer
- **`float()`** converts to decimal number
- **`str()`** converts to string
- **`bool()`** converts to True/False
- **Falsy values**: `""`, `0`,
