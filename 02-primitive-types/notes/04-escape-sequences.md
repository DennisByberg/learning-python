# Escape Sequences in Python

## What are Escape Sequences?

The **backslash `\`** is a special character in Python that creates escape sequences. These allow you to include special characters in strings that would otherwise be difficult or impossible to type.

## Comments vs Escape Sequences

```python
# This is a comment - ignored by Python
course = "Python \nProgramming"  # \n is an escape sequence
```

- **`#`** = Comment (ignored by Python)
- **`\`** = Escape character (creates special sequences)

## Common Escape Sequences

### New Line `\n`

Creates a line break in your string:

```python
course = "Python \nProgramming"
print(course)
```

**Output:**

```
Python
Programming
```

### Backslash `\\`

To include an actual backslash in your string, use two backslashes:

```python
path = "C:\\Users\\John\\Documents"
print(path)  # C:\Users\John\Documents
```

### Other Common Escape Sequences

```python
# Tab character
message = "Name:\tJohn"
print(message)  # Name:    John

# Double quote inside string
text = "He said \"Hello!\""
print(text)  # He said "Hello!"

# Single quote inside string
text = 'It\'s a beautiful day'
print(text)  # It's a beautiful day

# Carriage return
text = "Hello\rWorld"
print(text)  # World (overwrites "Hello")
```

## Complete List of Escape Sequences

| Sequence | Description     | Example            |
| -------- | --------------- | ------------------ |
| `\n`     | New line        | `"Line 1\nLine 2"` |
| `\\`     | Backslash       | `"C:\\folder"`     |
| `\"`     | Double quote    | `"He said \"Hi\""` |
| `\'`     | Single quote    | `'It\'s nice'`     |
| `\t`     | Tab             | `"Name:\tJohn"`    |
| `\r`     | Carriage return | `"Hello\rWorld"`   |

## Key Points

- **Backslash `\`** is the escape character in Python
- **`\n`** creates a new line
- **`\\`** creates an actual backslash character
- **Comments `#`** are ignored by Python
- Escape sequences work inside both single and double quotes
- Escape sequences are processed when the string is created, not when printed

## When to Use Escape Sequences

- Multi-line output without using triple quotes
- Including quotes inside strings
- File paths on Windows
- Formatting text
