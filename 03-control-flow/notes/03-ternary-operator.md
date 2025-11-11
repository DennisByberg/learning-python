# Ternary Operator

## What is the Ternary Operator?

A **one-line shorthand** for simple `if-else` statements.

## Traditional If-Else

```python
age = 18

if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

print(message)  # Eligible
```

## Ternary Operator

Same logic in **one line**:

```python
age = 18

message = "Eligible" if age >= 18 else "Not eligible"

print(message)  # Eligible
```

## Syntax

```python
value_if_true if condition else value_if_false
```

## More Examples

```python
# Simple
age = 12
status = "Adult" if age >= 18 else "Minor"

# With numbers
temperature = 25
weather = "Warm" if temperature > 20 else "Cold"

# Direct use
print("Pass" if score >= 50 else "Fail")
```

## Key Points

- **One-line shorthand** for simple `if-else`
- **Syntax**: `value_if_true if condition else value_if_false`
- Use for **simple conditions** only
- For complex logic, use traditional `if-else`
