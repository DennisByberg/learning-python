# For...Else

## What is For...Else?

A `for` loop can have an **`else` clause** that executes **only if the loop completes normally** (without `break`).

```python
for number in range(3):
    print("Attempt", number + 1)
else:
    print("Loop completed")
```

## With `break` Statement

If the loop is **interrupted** by `break`, the `else` block is **skipped**.

```python
successful = True

for number in range(3):
    print("Attempt", number + 1)
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# Output:
# Attempt 1
# Successful
# (else block is NOT executed)
```

## Without `break` Statement

If the loop completes **without** `break`, the `else` block **executes**.

```python
successful = False

for number in range(3):
    print("Attempt", number + 1)
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# Output:
# Attempt 1
# Attempt 2
# Attempt 3
# Attempted 3 times and failed
```

## Common Use Case

Useful for **search operations** - execute code if item is **not found**.

```python
# Search for a number
numbers = [1, 2, 3, 4, 5]
search = 7

for num in numbers:
    if num == search:
        print("Found!")
        break
else:
    print("Not found")  # Executes if loop completes without break
```

## Key Points

- **`else`** executes only if loop completes **without** `break`
- **Skipped** if `break` is used
- Useful for **search operations** and **retry logic**
- Not commonly used, but powerful when needed
