# Escape Sequences

## What are Escape Sequences?

The **backslash `\`** creates special characters in strings.

```python
course = "Python \nProgramming"  # \n is an escape sequence
```

## Common Escape Sequences

```python
# New Line
print("Python \nProgramming")
# Output:
# Python
# Programming

# Backslash
path = "C:\\Users\\John\\Documents"  # C:\Users\John\Documents

# Quotes
text = "He said \"Hello!\""      # Double quote
text = 'It\'s a beautiful day'   # Single quote

# Tab
message = "Name:\tJohn"          # Tab character
```

## Complete List

| Sequence | Description  | Example            |
| -------- | ------------ | ------------------ |
| `\n`     | New line     | `"Line 1\nLine 2"` |
| `\\`     | Backslash    | `"C:\\folder"`     |
| `\"`     | Double quote | `"He said \"Hi\""` |
| `\'`     | Single quote | `'It\'s nice'`     |
| `\t`     | Tab          | `"Name:\tJohn"`    |

## Key Points

- **Backslash `\`** is the escape character
- **`\n`** creates new lines
- **`\\`** creates actual backslash
- **`\"`** and **`\'`** for quotes inside strings
