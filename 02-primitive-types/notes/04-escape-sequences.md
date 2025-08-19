# Escape Sequences

## What are Escape Sequences?

The **backslash `\`** creates special characters in strings.

```python
# This is a comment - ignored by Python
course = "Python \nProgramming"  # \n is an escape sequence
```

- **`#`** = Comment (ignored by Python)
- **`\`** = Escape character (creates special sequences)

## Common Escape Sequences

### New Line `\n`

```python
course = "Python \nProgramming"
print(course)
# Output:
# Python
# Programming
```

### Backslash `\\`

```python
path = "C:\\Users\\John\\Documents"
print(path)  # C:\Users\John\Documents
```

### Other Sequences

```python
message = "Name:\tJohn"           # Tab character
text = "He said \"Hello!\""       # Double quote
text = 'It\'s a beautiful day'    # Single quote
text = "Hello\rWorld"             # Carriage return (overwrites)
```

## Complete List

| Sequence | Description     | Example            |
| -------- | --------------- | ------------------ |
| `\n`     | New line        | `"Line 1\nLine 2"` |
| `\\`     | Backslash       | `"C:\\folder"`     |
| `\"`     | Double quote    | `"He said \"Hi\""` |
| `\'`     | Single quote    | `'It\'s nice'`     |
| `\t`     | Tab             | `"Name:\tJohn"`    |
| `\r`     | Carriage return | `"Hello\rWorld"`   |

## Key Points

- **Backslash `\`** is the escape character
- **`\n`** creates new lines
- **`\\`** creates actual backslash
- Works inside single and double
