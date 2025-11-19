# Raising Exceptions

## Raising Exceptions Manually

Use **`raise`** to throw exceptions in your code.

```python
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age
```

## Catching Raised Exceptions

```python
try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)  # "Age cannot be 0 or less"
```

## Common Exception Types

```python
raise ValueError("Invalid value")     # Wrong value
raise TypeError("Wrong type")         # Wrong type
raise Exception("Generic error")      # Generic
```

## Re-raising

```python
try:
    calculate_xfactor(-1)
except ValueError as ex:
    print(f"Logging: {ex}")
    raise  # Re-raise same exception
```

## Key Points

- **`raise ExceptionType("message")`** - throw exception manually
- Use for **invalid input** or **illegal operations**
- Always provide **clear error messages**
- Handle with **try/except** like normal exceptions
- **`raise`** alone re-raises current exception
