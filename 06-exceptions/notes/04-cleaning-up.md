# Cleaning Up

## The Finally Block

**`finally`** runs **always** - whether an exception occurs or not. Perfect for cleanup tasks.

```python
try:
    file = open("data.txt")
    age = int(input("Age: "))
except ValueError:
    print("Invalid age")
finally:
    file.close()  # Always runs - cleanup guaranteed
```

## When Finally Runs

```python
try:
    print("Try block")
    # Code here
except ValueError:
    print("Exception handled")
else:
    print("No exception")
finally:
    print("Finally - always runs")
```

**All scenarios:**
- **No exception** → try → else → finally
- **Exception caught** → try → except → finally
- **Exception not caught** → try → finally → crash

## Common Use Case: File Handling

```python
file = None
try:
    file = open("exercises.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Invalid input")
finally:
    if file:
        file.close()  # Cleanup - file always closed
```

**Why `file = None`?** If `open()` fails, `file` won't exist in `finally`.

## Complete Structure

```python
try:
    # Code that might raise exception
    pass
except ExceptionType:
    # Handle exception
    pass
else:
    # Runs if no exception
    pass
finally:
    # Always runs - cleanup code
    pass
```

## Key Points

- **`finally`** - always executes, even if exception occurs
- Perfect for **cleanup**: closing files, releasing resources, etc.
- Runs **after** try/except/else blocks
- Runs even if exception isn't caught (before crash)
- Common pattern: initialize resource before `try`, clean up in `finally`
