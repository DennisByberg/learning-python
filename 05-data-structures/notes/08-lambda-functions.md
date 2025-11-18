# Lambda Functions

## What are Lambda Functions?

Lambda functions are **small anonymous functions** defined in a single line without using `def`.

## Syntax

```python
lambda parameters: expression
```

- **`lambda`** - keyword to define lambda
- **`parameters`** - input values (like function parameters)
- **`expression`** - single expression that gets returned

## Basic Example

### Regular Function

```python
def square(x):
    return x ** 2

print(square(5))  # 25
```

### Lambda Equivalent

```python
square = lambda x: x ** 2
print(square(5))  # 25
```

## Lambda with Multiple Parameters

```python
add = lambda x, y: x + y
print(add(3, 5))  # 8

multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # 24
```

## Common Use Cases

### 1. Sorting with key Parameter

```python
items = [("Product1", 20), ("Product2", 11), ("Product3", 22)]

# Without lambda (using function)
def get_price(item):
    return item[1]

items.sort(key=get_price)

# With lambda (cleaner)
items.sort(key=lambda item: item[1])
print(items)
# [("Product2", 11), ("Product1", 20), ("Product3", 22)]
```

### 2. Sorting by Different Criteria

```python
# Sort by name (first element)
items.sort(key=lambda item: item[0])

# Sort by price descending
items.sort(key=lambda item: item[1], reverse=True)

# Sort by string length
words = ["python", "is", "awesome"]
words.sort(key=lambda word: len(word))
print(words)  # ["is", "python", "awesome"]
```

### 3. With map() Function

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

### 4. With filter() Function

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]
```

## Lambda vs Regular Functions

```python
# Regular function - multiple lines, named
def is_even(x):
    return x % 2 == 0

# Lambda - single line, anonymous
is_even = lambda x: x % 2 == 0
```

## Limitations

### Cannot Have Multiple Statements

```python
# This doesn't work
lambda x:
    result = x ** 2
    return result

# Must be single expression
lambda x: x ** 2
```

### Cannot Have Annotations

```python
# Regular function with annotations
def add(x: int, y: int) -> int:
    return x + y

# Lambda - no annotations
add = lambda x, y: x + y
```

## When to Use Lambda

**Use Lambda When:**

- Function is simple (one expression)
- Used once (like with `sort`, `map`, `filter`)
- Improves readability

**Use Regular Function When:**

- Function is complex (multiple lines)
- Used multiple times
- Needs documentation
- Requires debugging

## Practical Examples

```python
# Sort people by age
people = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35)
]
people.sort(key=lambda person: person[1])
print(people)
# [("Bob", 25), ("Alice", 30), ("Charlie", 35)]

# Filter numbers greater than 5
numbers = [1, 6, 3, 8, 2, 9]
result = list(filter(lambda x: x > 5, numbers))
print(result)  # [6, 8, 9]

# Convert to uppercase
words = ["hello", "world"]
result = list(map(lambda word: word.upper(), words))
print(result)  # ["HELLO", "WORLD"]
```

## Key Points

- **Lambda** creates anonymous (unnamed) functions
- Syntax: `lambda parameters: expression`
- **Single expression** only - no multiple statements
- Commonly used with **`sort()`**, **`map()`**, **`filter()`**
- More **concise** than regular functions for simple operations
- **Cannot** have type annotations or docstrings
- Use for **short, simple** operations
- Use regular `def` for **complex** or **reusable** functions
- Lambda returns the expression result automatically
