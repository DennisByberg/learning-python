# Chaining Comparison Operators

## What is Chaining?

Python allows **chaining** comparison operators for cleaner, more readable code.

## Traditional Approach

Using **`and`** to combine conditions:

```python
age = 22

if age >= 18 and age < 65:
    print("Eligible")
```

## Chained Comparison

Same logic, **more readable**:

```python
age = 22

if 18 <= age < 65:
    print("Eligible")
```

**Reads like math**: "age is between 18 and 65"

## More Examples

```python
# Check if number is in range
x = 5
if 0 <= x <= 10:
    print("Valid range")

# Check if temperature is moderate
temperature = 25
if 20 < temperature < 30:
    print("Comfortable")

# Works with any comparison operators
score = 85
if 0 <= score <= 100:
    print("Valid score")
```

## How It Works

```python
# This:
if 18 <= age < 65:

# Is equivalent to:
if age >= 18 and age < 65:
```

## Key Points

- **Chaining** makes code more readable
- **Reads like mathematical notation**
- Equivalent to using **`and`**
- Works with any comparison operators (`<`, `<=`, `>`, `>=`, `==`, `!=`)
- More **Pythonic** style
