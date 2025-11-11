# String Methods

## Dot Notation

Strings are **objects** with methods accessed using **dot notation**.

```python
course = "  python programming"
course.upper()  # "  PYTHON PROGRAMMING"
```

## Common Methods

```python
course = "  python programming"

# Case conversion
course.upper()   # "  PYTHON PROGRAMMING"
course.lower()   # "  python programming"
course.title()   # "  Python Programming"

# Whitespace
course.strip()   # "python programming" - both ends
course.lstrip()  # left side only
course.rstrip()  # right side only

# Finding & Replacing
course.find("python")       # 2 (index)
course.find("Pro")          # -1 (not found - case sensitive)
course.replace("p", "j")    # "  jython jrogramming"

# Membership testing
"pro" in course             # True
"dennis" not in course      # True
```

## Key Points

- **Dot notation** accesses object methods
- **`find()` returns -1** when not found
- **Case sensitive** - "Pro" ≠ "pro"
- **Methods create new strings** - original unchanged
- **`in`/`not in`** return boolean values
