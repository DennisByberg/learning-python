# Types of Functions

## Two Types of Functions

Functions can either **perform a task** or **return a value**.

### 1. Functions That Perform a Task

These functions **do something** but don't return a value.

```python
def greet(name):
    print(f"Hi {name}")

greet("Dennis")  # Output: Hi Dennis
```

**Use case:** Printing, sending emails, saving to database, etc.

### 2. Functions That Return a Value

These functions **calculate and return** a value that can be used later.

```python
def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Dennis")
print(message)  # Output: Hi Dennis
```

**Use case:** Calculations, data processing, formatting, etc.

## The Return Statement

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8
```

- **`return`** sends a value back to the caller
- Function execution **stops** at the return statement
- Without `return`, a function returns `None` by default

## Default Return Value

```python
def say_hello():
    print("Hello!")

result = say_hello()  # Output: Hello!
print(result)         # Output: None
```

Functions without a `return` statement return `None`.

## Key Points

- Functions can **perform tasks** or **return values**
- Use **`return`** to send a value back to the caller
- Functions without `return` return `None` by default
- **Return stops** function execution immediately
- Returned values can be **stored in variables** or used directly
