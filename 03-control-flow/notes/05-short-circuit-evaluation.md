# Short Circuit Evaluation

## What is Short Circuit Evaluation?

Python **stops evaluating** conditions as soon as the result is determined.

## AND Operator (`and`)

If the **first** condition is `False`, Python **stops** - no need to check the rest.

```python
high_income = False
good_credit = True

# Python sees False and stops - doesn't check good_credit
if high_income and good_credit:
    print("Eligible")
```

**Why?** If one condition in `and` is `False`, the entire expression is `False`.

## OR Operator (`or`)

If the **first** condition is `True`, Python **stops** - no need to check the rest.

```python
high_income = True
good_credit = False

# Python sees True and stops - doesn't check good_credit
if high_income or good_credit:
    print("Eligible")
```

**Why?** If one condition in `or` is `True`, the entire expression is `True`.

## Why Does This Matter?

**Performance** - Python doesn't waste time evaluating unnecessary conditions.

```python
# Example: Avoid errors
age = 0

# Without short circuit, this could cause division by zero
if age > 0 and 100 / age > 5:
    print("Valid")
```

## Key Points

- **`and`** - Stops at first `False`
- **`or`** - Stops at first `True`
- Improves **performance**
- Can prevent **errors** in complex conditions
