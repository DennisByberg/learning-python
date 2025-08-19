# String Methods

## Object Methods with Dot Notation

Everything in Python is an **object**. Strings have methods accessed with **dot notation**.

```python
course = "  python programming"
course.upper()  # Access method with dot
```

## Common Methods

### Case Conversion

```python
course.upper()  # "  PYTHON PROGRAMMING"
course.lower()  # "  python programming"
course.title()  # "  Python Programming"
```

### Whitespace

```python
course.strip()   # "python programming" - both ends
course.lstrip()  # left side only
course.rstrip()  # right side only
```

### Finding & Replacing

```python
course.find("python")  # 2 (index)
course.find("Pro")     # -1 (not found - case sensitive)
course.replace("p", "j")  # "  jython jrogramming"
```

### Membership Testing

```python
"pro" in course      # True
"dennis" not in course  # True
```

## Key Points

- **Dot notation** accesses object methods
- **`find()` returns -1** when not found
- **Case sensitive** - "Pro" ≠ "pro"
- **Methods create new strings** - original unchanged
- **`in`/`not in`** return boolean values
