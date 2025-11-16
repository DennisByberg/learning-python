# Arguments

## What are Arguments?

Arguments are **values passed to a function** when calling it.

```python
def greet(first_name, last_name):
    print(f"Hi There {first_name} {last_name}")
    print("Welcome!")

greet("Dennis", "Byberg")
```

**Output:**

```
Hi There Dennis Byberg
Welcome!
```

## Parameters vs Arguments

```python
def greet(first_name, last_name):  # Parameters
    print(f"Hi {first_name} {last_name}")

greet("Dennis", "Byberg")  # Arguments
```

- **Parameters** - variables in the function definition
- **Arguments** - actual values passed when calling the function

## Positional Arguments

Arguments are matched to parameters **by position**.

```python
def introduce(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

introduce("Alice", 25, "Stockholm")  # Correct order
introduce(25, "Alice", "Stockholm")  # Wrong! Order matters
```

## Multiple Arguments

```python
def calculate_total(price, tax, discount):
    total = price + tax - discount
    print(f"Total: {total}")

calculate_total(100, 25, 10)  # Total: 115
```

## Key Points

- **Arguments** are values passed to functions
- **Parameters** are variables in function definition
- **Positional arguments** must match the order of parameters
- You can pass **multiple arguments** separated by commas
- Arguments make functions **flexible and reusable**
