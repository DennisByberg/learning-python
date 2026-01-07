# xargs (Arbitrary Arguments)

## What are xargs?

**`*args`** allows a function to accept **any number of arguments**.

```python
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2, 3, 4, 5))  # 120
print(multiply(2, 3))         # 6
print(multiply(10))           # 10
```

## How It Works

The `*` operator **collects all arguments into a tuple**.

```python
def print_numbers(*numbers):
    print(type(numbers))  # <class 'tuple'>
    print(numbers)

print_numbers(1, 2, 3, 4, 5)
# Output:
# <class 'tuple'>
# (1, 2, 3, 4, 5)
```

## Iterating Over xargs

Since `*args` is a **tuple**, you can loop through it.

```python
def sum_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(10, 20, 30, 40)) # 100
```

## Combining with Regular Parameters

**Required parameters must come before `*args`.**

```python
def greet(greeting, *names):
    for name in names:
        print(f"{greeting} {name}!")

greet("Hello", "Alice", "Bob", "Charlie")
# Output:
# Hello Alice!
# Hello Bob!
# Hello Charlie!
```

## Common Naming Convention

While you can use any name, **`*args`** is the standard convention.

```python
# Standard (preferred)
def func(*args):
    pass

# Valid but uncommon
def func(*numbers):
    pass
```

## Key Points

- **`*args`** accepts any number of arguments
- Arguments are collected into a **tuple**
- Can **iterate** over `*args` like any tuple
- **Required parameters must come before** `*args`
- Standard naming convention is **`*args`**
- Useful when you don't know how many arguments will be passed
