# Formatted Strings

## F-String Syntax

Use `f` before quotes and put variables inside `{}`:

```python
first = "Dennis"
last = "Byberg"

full_name = f"{first} {last}"  # Dennis Byberg
```

## Why F-Strings?

### Old Methods

```python
# String concatenation - messy
full_name = first + " " + last

# .format() method - verbose
full_name = "{} {}".format(first, last)
```

### Modern F-Strings

```python
# Clean and readable
full_name = f"{first} {last}"
```

## Examples

### Variables and Expressions

```python
name = "Alice"
age = 25

message = f"Hello, I'm {name} and I'm {age} years old"
result = f"Sum: {5 + 3}"  # Sum: 8
```

### Function Calls

```python
course = "Python Programming"
info = f"Course '{course}' has {len(course)} characters"
```

### Number Formatting

```python
price = 19.99567
formatted = f"Price: ${price:.2f}"  # Price: $19.99
```

## Key Points

- **F-strings** start with `f` before quotes
- **Variables/expressions** go inside `{}`
- **Modern and readable** - preferred method
- \*\*Available in Python 3.6
