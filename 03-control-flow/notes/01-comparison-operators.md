# Comparison Operators

## What are Comparison Operators?

Comparison operators **compare values** and return a boolean (`True` or `False`).

```python
print(10 > 3)   # True  - Greater than
print(10 >= 3)  # True  - Greater than or equal to
print(10 < 3)   # False - Less than
print(10 <= 3)  # False - Less than or equal to
print(10 == 3)  # False - Equal to
print(10 != 3)  # True  - Not equal to
```

## Comparing Different Types

```python
print(10 == "10")  # False
```

**Why?** Different types are **not equal**. `10` is an **int**, `"10"` is a **string**.

## Comparing Strings

Strings are compared using **Unicode values**.

```python
print("bag" > "apple")  # True  - "b" (98) > "a" (97)
print("bag" > "BAG")    # True  - "b" (98) > "B" (66)
```

**Lowercase letters have higher Unicode values than uppercase.**

```python
print(ord("b"))  # 98
print(ord("B"))  # 66
print(ord("a"))  # 97
```

## Key Points

- **Comparison operators** return `True` or `False`
- **Different types** are not equal (`10 != "10"`)
- **Strings** are compared using Unicode values
- **Lowercase > Uppercase** (`"a"` > `"A"`)
- **`ord()`** returns the Unicode value of a character
