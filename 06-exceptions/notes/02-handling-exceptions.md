# Handling Exceptions

## Try/Except Block

Use **try/except** to catch and handle exceptions without crashing.

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("Invalid age")
    age = 0
```

## How It Works

1. Code in **`try`** block runs first
2. If an exception occurs, jump to **`except`** block
3. Program continues after the try/except

```python
try:
    age = int(input("Age: "))  # User types "abc"
    # This line is skipped if error occurs
    print("Age entered successfully")
except ValueError:
    print("You didn't enter a valid age")  # This runs instead
# Program continues here
print("Execution continues")
```

## Capturing Exception Object

Use **`as`** to get the exception object and its details.

```python
try:
    age = int(input("Age: "))
except ValueError as ex:
    print(f"Error: {ex}")
    print(f"Type: {type(ex)}")
```

**Output when user types "abc":**

```
Error: invalid literal for int() with base 10: 'abc'
Type: <class 'ValueError'>
```

## The Else Clause

**`else`** block runs only if **no exception** occurred.

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("Invalid age")
else:
    print("No exceptions were thrown")
```

- **Exception occurs** → `except` runs, `else` skipped
- **No exception** → `except` skipped, `else` runs

## Complete Example

```python
try:
    age = int(input("Age: "))
except ValueError as ex:
    print(f"Invalid input: {ex}")
else:
    print(f"Age {age} is valid")
print("Program continues")
```

**Scenario 1:** User enters `25`

```
Age 25 is valid
Program continues
```

**Scenario 2:** User enters `abc`

```
Invalid input: invalid literal for int() with base 10: 'abc'
Program continues
```

## Key Points

- **`try`** - code that might raise an exception
- **`except ExceptionType`** - handles specific exception
- **`as ex`** - captures exception object for details
- **`else`** - runs only if no exception occurred
- Program **continues** after try/except (no crash)
