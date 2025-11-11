# Logical Operators

## What are Logical Operators?

Combine multiple conditions using **`and`**, **`or`**, and **`not`**.

```python
high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible")
```

## The Three Logical Operators

### AND Operator

**Both** conditions must be `True`.

```python
high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible")  # Executes (both True)
```

### OR Operator

**At least one** condition must be `True`.

```python
high_income = False
good_credit = True

if high_income or good_credit:
    print("Eligible")  # Executes (one is True)
```

### NOT Operator

**Inverts** the boolean value.

```python
student = False

if not student:
    print("Not a student")  # Executes (not False = True)
```

## Combining Operators

Use **parentheses** for complex conditions.

```python
high_income = False
good_credit = True
student = True

# (high_income OR good_credit) AND (NOT student)
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")  # Executes
```

## Truth Tables

```python
# AND - both must be True
True and True   # True
True and False  # False
False and False # False

# OR - at least one must be True
True or True    # True
True or False   # True
False or False  # False

# NOT - inverts value
not True   # False
not False  # True
```

## Key Points

- **`and`** - Both conditions must be `True`
- **`or`** - At least one condition must be `True`
- **`not`** - Inverts the boolean value
- Use **parentheses** for complex conditions
- **Order of evaluation**: `not` → `and` → `or`
