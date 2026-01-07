# Defining Functions

## What are Functions?

Functions are **reusable blocks of code** that perform a specific task.

```python
def greet_user():
    print("Hi There!")
    print("Welcome!")

greet_user()  # Call the function
```

**Output:**

```
Hi There!
Welcome!
```

## Function Syntax

```python
def function_name():
    # Code block
    # Indented with 4 spaces
    statement1
    statement2
```

- **`def`** - keyword to define a function
- **`function_name`** - descriptive name in snake_case
- **`()`** - parentheses (required, even if empty)
- **`:`** - colon to start the code block
- **Indentation** - 4 spaces for function body

## Calling Functions

```python
def say_hello():
    print("Hello!")

say_hello()  # Executes the function
say_hello()  # Can call multiple times
```

**Output:**

```
Hello!
Hello!
```

## Naming Conventions

Use **snake_case** for function names:

```python
# Good
def calculate_total():
    pass

def send_email():
    pass

# Avoid
def calculateTotal():
    pass

def SendEmail():
    pass
```

## Key Points

- Functions are **reusable code blocks**
- Use **`def`** keyword to define functions
- Function names use **snake_case**
- **Parentheses `()`** are required
- **Call** the function to execute it: `function_name()`
- Functions must be **defined before** they are called
