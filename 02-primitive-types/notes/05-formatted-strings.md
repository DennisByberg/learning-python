# Formatted Strings

## F-String Syntax

Use `f` before quotes and put variables inside `{}`:

```python
first = "John"
last = "Doe"

full_name = f"{first} {last}"  # John Doe
```

## Why F-Strings?

```python
# Old - String concatenation (messy)
full_name = first + " " + last

# Old - .format() method (verbose)
full_name = "{} {}".format(first, last)

# Modern - F-strings (clean and readable)
full_name = f"{first} {last}"
```

## Examples

```python
# Variables and expressions
name = "Alice"
age = 25
message = f"Hello, I'm {name} and I'm {age} years old"
result = f"Sum: {5 + 3}"  # Sum: 8

# Function calls
course = "Python Programming"
info = f"Course '{course}' has {len(course)} characters"

# Number formatting
price = 19.99567
formatted = f"Price: ${price:.2f}"  # Price: $19.99
```

## Key Points

- **F-strings** start with `f` before quotes
- **Variables/expressions** go inside `{}`
- **Modern and readable** - preferred method
- **Available in Python 3.6+**
