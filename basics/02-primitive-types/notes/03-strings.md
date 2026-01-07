# Strings

## Creating Strings

```python
course = 'Python Programming'  # Single quotes
course = "Python Programming"  # Double quotes

# Triple quotes (multi-line)
message = """
This is a multi-line string.
It can span across multiple lines.
"""
```

## String Length

```python
course = "Python Programming"
print(len(course))  # 18
```

## Accessing Characters

```python
course = "Python Programming"

print(course[0])   # P  (first character)
print(course[1])   # y  (second character)
print(course[-1])  # g  (last character)
print(course[-2])  # n  (second to last)
```

**Python is zero-indexed** - counting starts from 0.

## String Slicing

```python
course = "Python Programming"

print(course[0:3])  # Pyt
print(course[7:18]) # Programming
print(course[:3])   # Pyt - from start
print(course[0:])   # Python Programming - to end
print(course[:])    # Python Programming - entire string
```

**Slicing format:** `[start:end]` (end not included)

## Key Points

- **Single, double, or triple quotes** for strings
- **`len()`** returns character count
- **Zero-indexed** - first character is `[0]`
- **Negative indexing** counts from end
- **Slicing** uses `[start:end]` format
