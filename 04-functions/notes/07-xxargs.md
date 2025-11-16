# xxargs (Keyword Arguments)

## What are xxargs?

**`**kwargs`** allows a function to accept **any number of keyword arguments**.

```python
def save_user(**user):
    print(user)

save_user(id=1, name="John", age=22)
# Output: {'id': 1, 'name': 'John', 'age': 22}
```

## How It Works

The `**` operator **collects all keyword arguments into a dictionary**.

```python
def print_user(**user):
    print(type(user))  # <class 'dict'>
    print(user)

print_user(name="Alice", age=25, city="Stockholm")
# Output:
# <class 'dict'>
# {'name': 'Alice', 'age': 25, 'city': 'Stockholm'}
```

## Accessing Dictionary Values

Since `**kwargs` is a **dictionary**, you can access values by key.

```python
def greet_user(**user):
    print(f"Hello {user['name']}!")
    print(f"You are {user['age']} years old")

greet_user(name="Bob", age=30)
# Output:
# Hello Bob!
# You are 30 years old
```

## Iterating Over xxargs

```python
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Charlie", age=35, country="Norway")
# Output:
# name: Charlie
# age: 35
# country: Norway
```

## Combining Parameters

**Order matters:** regular → `*args` → `**kwargs`

```python
def create_user(username, *hobbies, **details):
    print(f"Username: {username}")
    print(f"Hobbies: {hobbies}")
    print(f"Details: {details}")

create_user("alice123", "reading", "gaming", age=25, city="Stockholm")
# Output:
# Username: alice123
# Hobbies: ('reading', 'gaming')
# Details: {'age': 25, 'city': 'Stockholm'}
```

## Common Naming Convention

While you can use any name, **`**kwargs`** is the standard convention.

```python
# Standard (preferred)
def func(**kwargs):
    pass

# Valid but uncommon
def func(**user):
    pass
```

## Key Points

- **`**kwargs`** accepts any number of keyword arguments
- Arguments are collected into a **dictionary**
- Access values using **dictionary syntax**: `kwargs['key']`
- Can **iterate** over `**kwargs` using `.items()`
- Parameter order: regular → `*args` → `**kwargs`
- Standard naming convention is **`**kwargs`**
- Useful for flexible function signatures
