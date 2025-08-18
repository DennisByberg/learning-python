# Variables

## What are Variables?

Variables are used to **store data in computer memory**. Think of a variable as a labeled box where you can put information that your program can use later.

```python
students_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
```

## Key Rules

### Python is Case Sensitive

```python
name = "John"
Name = "Jane"
NAME = "Bob"
# These are three DIFFERENT variables!
```

### Variable Naming Rules

**Valid names:**

```python
age = 25
first_name = "Alice"
student_count = 100
_private_var = "hidden"
course2024 = "Python"
```

**Invalid names:**

```python
2students = 100      # Cannot start with number
first-name = "Bob"   # Hyphens not allowed
class = "Math"       # 'class' is a reserved keyword
```

### Naming Convention

Use **snake_case** in Python:

```python
# Good
student_count = 1000
course_name = "Python"

# Avoid
studentCount = 1000
courseName = "Python"
```

## Reassigning Variables

Variables can be changed:

```python
count = 5
print(count)  # 5

count = 10
print(count)  # 10
```

## Key Takeaways

- Variables store data in computer memory
- **Python is case sensitive** - `name` ≠ `Name`
- Use snake_case naming convention
- Use descriptive names that explain what the variable contains
- Variables can be
