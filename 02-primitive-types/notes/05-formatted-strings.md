# Formatted Strings

## What are Formatted Strings?

Formatted strings (f-strings) are a modern way to combine variables and text in Python. They make it easy to insert variable values into strings.

## F-String Syntax

Use `f` before the opening quote and put variables inside curly braces `{}`:

```python
first = "Dennis"
last = "Byberg"

# F-string - modern approach
full_name = f"{first} {last}"
print(full_name)  # Dennis Byberg
```

## Why Use F-Strings?

### Before F-Strings (Old Methods)

```python
first = "Dennis"
last = "Byberg"

# String concatenation - harder to read
full_name = first + " " + last

# .format() method - more verbose
full_name = "{} {}".format(first, last)

# % formatting - outdated
full_name = "%s %s" % (first, last)
```

### With F-Strings (Modern)

```python
first = "Dennis"
last = "Byberg"

# Clean and readable
full_name = f"{first} {last}"
```

## F-String Examples

### Basic Variable Insertion

```python
name = "Alice"
age = 25

message = f"Hello, my name is {name} and I am {age} years old"
print(message)  # Hello, my name is Alice and I am 25 years old
```

### Expressions Inside F-Strings

You can put any Python expression inside the curly braces:

```python
a = 5
b = 3

result = f"The sum of {a} and {b} is {a + b}"
print(result)  # The sum of 5 and 3 is 8
```

### Function Calls in F-Strings

```python
name = "Python Programming"
message = f"The course '{name}' has {len(name)} characters"
print(message)  # The course 'Python Programming' has 18 characters
```

## Real Example from Our Code

```python
first = "Dennis"
last = "Byberg"

full_name = f"{first} {last}"
full_name_length = len(full_name)

print(full_name)        # Dennis Byberg
print(full_name_length) # 13
```

## Advanced F-String Features

### Formatting Numbers

```python
price = 19.99567
formatted_price = f"Price: ${price:.2f}"
print(formatted_price)  # Price: $19.99
```

### Multi-line F-Strings

```python
name = "John"
age = 30
city = "Stockholm"

info = f"""
Name: {name}
Age: {age}
City: {city}
"""
print(info)
```

## Key Points

- **F-strings** start with `f` before the quote
- **Variables** go inside curly braces `{}`
- **Expressions** can be evaluated inside `{}`
- **Functions** can be called inside `{}`
- **Modern and readable** - preferred over older string formatting methods
- **Available in Python 3.6+**

## Best Practices

```python
# Good - clear and readable
name = "Alice"
age = 25
message = f"Hello {name}, you are {age} years old"

# Avoid - harder to read
message = "Hello " + name + ", you are " + str(age) + " years old"
```

F-strings make your code cleaner and easier to understand!
