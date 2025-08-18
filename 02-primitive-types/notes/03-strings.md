# Strings

## Creating Strings

### Different Quote Types

```python
# Single quotes
course = 'Python Programming'

# Double quotes
course = "Python Programming"

# Triple quotes (for multi-line strings)
message = """
This is a multi-line string.
It can span across multiple lines.
Very useful for long text.
"""
```

## String Length

### The `len()` Function

Use the `len()` function to get the number of characters in a string:

```python
course = "Python Programming"
print(len(course))  # 18
```

**Calling a function** means using it by writing its name followed by parentheses. The value you put inside the parentheses is called an **argument** (or **arg**).

```python
len(course)  # 'course' is the argument we pass to the len function
```

## Accessing Individual Characters

### Square Brackets and Zero Indexing

Use **square brackets** `[]` to get a specific character from a string.

**Python is zero-indexed** - counting starts from 0, not 1:

```python
course = "Python Programming"

print(course[0])   # P  (first character)
print(course[1])   # y  (second character)
print(course[2])   # t  (third character)
```

### Negative Indexing

Use negative numbers to count from the end:

```python
course = "Python Programming"

print(course[-1])  # g  (last character)
print(course[-2])  # n  (second to last)
```

## String Slicing

### Getting Multiple Characters

Use **slicing** to get a portion of a string with the format `[start:end]`:

```python
course = "Python Programming"

print(course[0:3])  # Pyt  (characters 0, 1, 2)
print(course[7:18]) # Programming
```

### Slicing Shortcuts

```python
course = "Python Programming"

# From start to position 3
print(course[:3])   # Pyt

# From position 0 to end
print(course[0:])   # Python Programming

# Entire string (copy)
print(course[:])    # Python Programming
```

## Slicing Examples

```python
course = "Python Programming"

print(course[0:3])  # Pyt    - from index 0 to 3 (not including 3)
print(course[0:])   # Python Programming - from index 0 to end
print(course[:3])   # Pyt    - from start to index 3 (not including 3)
print(course[:])    # Python Programming - entire string
```

## Key Points

- **Strings** can use single, double, or triple quotes
- **`len()`** function returns the number of characters
- **Arguments** are values passed to functions inside parentheses
- **Zero-indexed** means counting starts from 0
- **Square brackets** `[]` access individual characters
- **Slicing** `[start:end]` gets multiple characters
- **Negative indexing** counts from the end of the string
