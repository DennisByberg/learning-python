# Scope

## What is Scope?

Scope determines **where a variable can be accessed** in your code.

```python
message = "a"  # Global scope

def greet(name):
    message = "b"  # Local scope
    print(message)

greet("Dennis")  # Output: b
print(message)   # Output: a
```

## Local Scope

Variables defined **inside a function** are local - only accessible within that function.

```python
def calculate():
    result = 10 + 5  # Local variable
    print(result)

calculate()       # 15
print(result)     # NameError: name 'result' is not defined
```

## Global Scope

Variables defined **outside functions** are global - accessible everywhere.

```python
count = 0  # Global variable

def increment():
    print(count)  # Can READ global variables

increment()  # 0
print(count) # 0
```

## The Global Keyword

Use `global` to **modify** a global variable inside a function.

```python
message = "a"

def greet(name):
    global message  # Access global variable
    message = "b"   # Modify it

greet("Dennis")
print(message)  # Output: b
```

**⚠️ BAD PRACTICE!** Avoid using `global` - it makes code hard to debug and maintain.

## Better Approach: Return Values

Instead of modifying global variables, **return values** from functions.

```python
# Bad (using global)
message = "a"

def greet(name):
    global message
    message = "b"

greet("Dennis")
print(message)

# Good (using return)
def greet(name):
    return "b"

message = "a"
message = greet("Dennis")
print(message)  # b
```

## Key Points

- **Local scope**: Variables inside functions
- **Global scope**: Variables outside functions
- Functions can **read** global variables without `global` keyword
- Use **`global`** keyword to modify global variables (avoid this!)
- **Best practice**: Use function parameters and return values instead
- Global variables make code harder to understand and debug
