# List Unpacking

## What is List Unpacking?

List unpacking allows you to **assign list items to multiple variables** in one line.

## Basic Unpacking

```python
numbers = [1, 2, 3]
first, second, third = numbers

print(first)   # 1
print(second)  # 2
print(third)   # 3
```

**Important:** Number of variables **must match** number of items!

```python
numbers = [1, 2, 3]
a, b = numbers  # ValueError: too many values to unpack
```

## Unpacking with * (Rest Operator)

Use `*` to capture **remaining items** into a list.

```python
numbers = [1, 2, 3, 4, 5]
first, *rest = numbers

print(first)  # 1
print(rest)   # [2, 3, 4, 5]
```

## Unpacking First and Last

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
first, *middle, last = numbers

print(first)   # 1
print(middle)  # [2, 3, 4, 5, 6, 7]
print(last)    # 8
```

## Unpacking in the Middle

```python
numbers = [1, 2, 3, 4, 5]
first, second, *rest = numbers

print(first)   # 1
print(second)  # 2
print(rest)    # [3, 4, 5]
```

## Ignoring Values

Use `_` (underscore) for values you don't need.

```python
numbers = [1, 2, 3, 4, 5]
first, _, _, _, last = numbers

print(first)  # 1
print(last)   # 5
# The middle values (2, 3, 4) are ignored
```

## Combining _ with *

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
first, *_, last = numbers

print(first)  # 1
print(last)   # 8
# Everything in between is ignored
```

## Practical Example

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
first, *numbers_between, last = numbers

print(f"First number is: {first}")
print(f"Last number is: {last}")
print(f"Numbers between: {len(numbers_between)}")
```

**Output:**
```
First number is: 1
Last number is: 8
Numbers between: 6
```

## Key Points

- **Unpacking** assigns list items to variables in one line
- Number of variables must **match** number of items (unless using `*`)
- **`*variable`** captures remaining items into a list
- Use **`_`** to ignore values you don't need
- `*` can appear anywhere: start, middle, or end
- Makes code **cleaner** and more **readable**
- Only **one `*` operator** per unpacking
