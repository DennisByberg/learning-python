# Keyword Arguments

## What are Keyword Arguments?

Keyword arguments let you **specify arguments by name** instead of position.

```python
def increment(number, by):
    return number + by

print(increment(2, by=1))  # 3
```

## Positional vs Keyword Arguments

```python
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")

# Positional arguments (order matters)
greet("Dennis", "Byberg")

# Keyword arguments (order doesn't matter)
greet(last_name="Byberg", first_name="Dennis")
greet(first_name="Dennis", last_name="Byberg")
```

**Both produce:** `Hi Dennis Byberg`

## Why Use Keyword Arguments?

**1. Improves readability:**

```python
def send_email(to, subject, body):
    print(f"Sending to {to}: {subject}")

# Hard to read
send_email("alice@example.com", "Hello", "Welcome!")

# Clear and readable
send_email(to="alice@example.com", subject="Hello", body="Welcome!")
```

**2. Order doesn't matter:**

```python
send_email(body="Welcome!", to="alice@example.com", subject="Hello")
```

## Mixing Positional and Keyword Arguments

You can mix both, but **positional arguments must come first**.

```python
def calculate(a, b, c):
    return a + b + c

# Valid
print(calculate(1, 2, c=3))      # 6
print(calculate(1, b=2, c=3))    # 6

# Invalid
print(calculate(a=1, 2, 3))      # SyntaxError!
```

## Key Points

- **Keyword arguments** specify arguments by parameter name
- Use format: `parameter_name=value`
- **Order doesn't matter** with keyword arguments
- **Improves code readability** - makes intent clear
- **Positional arguments must come before** keyword arguments
- Especially useful for functions with many parameters
