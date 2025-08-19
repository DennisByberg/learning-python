# Working With Numbers

## Built-in Functions

Python has built-in functions for common number operations:

```python
print(round(2.9))    # 3 - Round to nearest integer
print(round(2.2))    # 2
print(abs(-2.9))     # 2.9 - Absolute value
```

## Math Module

Import the **math module** for advanced mathematical functions:

```python
import math

print(math.ceil(2.2))   # 3 - Ceiling (round up)
print(math.floor(2.9))  # 2 - Floor (round down)
```

### Common Math Functions

```python
import math

# Square root
sqrt = math.sqrt(10)
print(sqrt)  # 3.1622776601683795

# Power and logarithms
print(math.pow(2, 3))    # 8.0 - 2 to the power of 3
print(math.log(10))      # 2.302585092994046 - Natural log

# Trigonometry
print(math.sin(math.pi / 2))  # 1.0
print(math.cos(0))            # 1.0

# Constants
print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045
```

### Checking Numbers

```python
import math

print(math.isnan(True))   # False - Check if Not a Number
print(math.isinf(float('inf')))  # True - Check if infinite
```

## Key Points

- **Built-in functions**: `round()`, `abs()`
- **Import math module** for advanced functions
- **`math.ceil()`** rounds up, **`math.floor()`** rounds down
- **`math.sqrt()`** for square root
- **Google "Python 3 math module"** for complete documentation
