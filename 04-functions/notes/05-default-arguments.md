# Default Arguments

## What are Default Arguments?

Default arguments are **parameters with default values** that are used when no argument is provided.

```python
def increment(number, by=1):
    return number + by

print(increment(2))     # 3 (uses default by=1)
print(increment(2, 5))  # 7 (overrides default)
```

## Why Use Default Arguments?

Makes functions **more flexible** without requiring all arguments every time.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting} {name}!")

greet("Dennis")              # Hello Dennis!
greet("Dennis", "Hi")        # Hi Dennis!
greet("Dennis", "Welcome")   # Welcome Dennis!
```

## Multiple Default Arguments

```python
def create_user(name, age=18, country="Sweden"):
    print(f"{name}, {age}, {country}")

create_user("Alice")                    # Alice, 18, Sweden
create_user("Bob", 25)                  # Bob, 25, Sweden
create_user("Charlie", 30, "Norway")    # Charlie, 30, Norway
```

## Important Rules

**1. Default parameters must come after non-default parameters:**

```python
# Valid
def func(a, b, c=3):
    pass

# Invalid
def func(a, b=2, c):  # SyntaxError!
    pass
```

**2. Default values are evaluated once at definition:**

```python
def add_item(item, items=[]):  # Careful!
    items.append(item)
    return items

print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['apple', 'banana'] - Unexpected!
```

**Better approach:**

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## Key Points

- **Default arguments** provide fallback values for parameters
- Use format: `parameter=default_value`
- Makes functions **more flexible** - arguments become optional
- **Default parameters must come after** required parameters
- Can override defaults by providing arguments
- Useful for common use cases with sensible defaults
