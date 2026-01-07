# Exceptions

## What is an Exception?

An exception is an **error** that occurs during program execution, causing it to **crash** if not handled.

## Common Exception Types

| Exception           | Description           | Example               |
| ------------------- | --------------------- | --------------------- |
| `ValueError`        | Invalid value         | `int("abc")`          |
| `IndexError`        | Index out of range    | `[1, 2][5]`           |
| `KeyError`          | Key not in dictionary | `{"a": 1}["b"]`       |
| `ZeroDivisionError` | Division by zero      | `10 / 0`              |
| `FileNotFoundError` | File doesn't exist    | `open("missing.txt")` |

## Example

```python
# Without handling - program crashes
age = int(input("Age: "))  # User types "twenty" → ValueError

# With handling - program continues
try:
    age = int(input("Age: "))
except ValueError:
    print("Invalid age")
    age = 0
```

## Key Points

- **Unhandled exceptions** crash your program
- Use **try/except** to handle exceptions gracefully
- Makes programs **robust** and **user-friendly**
