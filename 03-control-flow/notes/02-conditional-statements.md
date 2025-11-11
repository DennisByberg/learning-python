# Conditional Statements

## If Statement

Execute code **only if** a condition is `True`.

```python
temperature = 35

if temperature > 30:
    print("It's warm")
    print("Drink water")
```

**Indentation matters!** Code inside `if` must be indented (4 spaces or 1 tab).

## If-Else Statement

Execute one block if `True`, another if `False`.

```python
temperature = 15

if temperature > 30:
    print("It's warm")
else:
    print("It's cold")
```

## If-Elif-Else Statement

Check **multiple conditions** in order.

```python
temperature = 25

if temperature > 30:
    print("It's warm")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
```

**Execution order:**

1. Check `if` condition
2. If `False`, check `elif` condition
3. If `False`, execute `else` block

## Code Outside Conditionals

Code **not indented** runs regardless of conditions.

```python
temperature = 15

if temperature > 30:
    print("It's warm")
else:
    print("It's cold")

print("Done")  # Always executes
```

## Key Points

- **Indentation** defines code blocks (4 spaces or 1 tab)
- **`if`** - Execute if condition is `True`
- **`elif`** - Check another condition if previous was `False`
- **`else`** - Execute if all conditions are `False`
- Code **outside** conditionals always executes
