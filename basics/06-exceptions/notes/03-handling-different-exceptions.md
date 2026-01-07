# Handling Different Exceptions

## Multiple Except Blocks

Handle different exceptions with separate **`except`** blocks.

```python
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("You didn't enter a valid number")
except ZeroDivisionError:
    print("Age cannot be 0")
```

- **`ValueError`** → user enters "abc"
- **`ZeroDivisionError`** → user enters 0

## Handling Multiple Exceptions the Same Way

Use a **tuple** to catch multiple exceptions with the same handler.

```python
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
```

Both `ValueError` and `ZeroDivisionError` trigger the same message.

## Separate Handlers vs Tuple

### Separate Handlers

```python
try:
    age = int(input("Age: "))
    result = 10 / age
except ValueError:
    print("Invalid number format")
except ZeroDivisionError:
    print("Division by zero not allowed")
```

**Benefits:** Different messages for different errors

### Tuple Handler

```python
try:
    age = int(input("Age: "))
    result = 10 / age
except (ValueError, ZeroDivisionError):
    print("Invalid input")
```

**Benefits:** Less code when same action needed

## Catching All Exceptions

Use **`Exception`** to catch any exception (use carefully).

```python
try:
    age = int(input("Age: "))
    result = 10 / age
except Exception as ex:
    print(f"Something went wrong: {ex}")
```

**Warning:** Too broad - hides unexpected errors. Be specific when possible.

## Order Matters

Put **specific exceptions first**, then more general ones.

```python
try:
    # code
except ValueError:
    print("Invalid value")
except Exception:  # Catch-all goes last
    print("Unexpected error")
```

## Key Points

- **Multiple `except` blocks** - handle each exception differently
- **Tuple of exceptions** - `except (Type1, Type2)` - same handler for multiple
- **Order matters** - specific exceptions before general ones
- **`Exception`** - catches all, but use specific types when possible
