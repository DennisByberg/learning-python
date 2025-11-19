# The With Statement

## What is With?

**`with`** automatically handles resource cleanup - no need for `finally` to close files.

```python
# Old way - manual cleanup
file = open("data.txt")
try:
    print(file.read())
finally:
    file.close()  # Must remember to close

# With statement - automatic cleanup
with open("data.txt") as file:
    print(file.read())
# File automatically closed here
```

## How It Works

The `with` statement automatically calls cleanup methods when the block ends.

```python
with open("exercises.py") as file:
    print("File opened")
    content = file.read()
# File automatically closed - even if exception occurs
```

## With in Try/Except

Combine `with` for cleanup and `try/except` for error handling.

```python
try:
    with open("exercises.py") as file:
        print("File opened")

    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")
```

File is closed automatically after the `with` block, even if exception occurs.

## Multiple Resources

Open multiple files in one `with` statement.

```python
with open("input.txt") as infile, open("output.txt", "w") as outfile:
    content = infile.read()
    outfile.write(content.upper())
# Both files automatically closed
```

## Benefits

**Without `with`:**

```python
file = None
try:
    file = open("data.txt")
    # Use file
except Exception:
    # Handle error
finally:
    if file:
        file.close()  # Manual cleanup
```

**With `with`:**

```python
try:
    with open("data.txt") as file:
        # Use file
        pass  # File auto-closed after this block
except Exception:
    # Handle error
    pass
```

Shorter, cleaner, safer!

## Key Points

- **`with`** - automatic resource cleanup
- No need for `finally` to close files
- File closes **automatically** when block ends
- Works even if **exception occurs**
- **Cleaner code** - less boilerplate
- Use for: files, database connections, network sockets
- Can open **multiple resources** in one statement
