# Looping Over Lists

## What is Looping Over Lists?

Looping allows you to **iterate through each item** in a list and perform actions on them.

## Basic For Loop

```python
letters = ["a", "b", "c"]

for letter in letters:
    print(letter)
```

**Output:**

```
a
b
c
```

## Looping with Index

Sometimes you need both the **index** and the **value**.

### Using range() and len()

```python
letters = ["a", "b", "c"]

for i in range(len(letters)):
    print(i, letters[i])
```

**Output:**

```
0 a
1 b
2 c
```

## Using enumerate()

`enumerate()` provides both **index** and **value** automatically.

```python
letters = ["a", "b", "c"]

for index, letter in enumerate(letters):
    print(index, letter)
```

**Output:**

```
0 a
1 b
2 c
```

### enumerate() Returns Tuples

```python
letters = ["a", "b", "c"]

for item in enumerate(letters):
    print(item)
```

**Output:**

```
(0, 'a')
(1, 'b')
(2, 'c')
```

Each item is a **tuple** `(index, value)` that can be unpacked:

```python
for item in enumerate(letters):
    print(item[0], item[1])  # Access by index

# Better: unpack directly
for index, letter in enumerate(letters):
    print(index, letter)
```

## Custom Start Index

`enumerate()` can start from a different number.

```python
letters = ["a", "b", "c"]

for index, letter in enumerate(letters, start=1):
    print(index, letter)
```

**Output:**

```
1 a
2 b
3 c
```

## Modifying Items While Looping

```python
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)  # [2, 4, 6, 8, 10]
```

## Looping Over Nested Lists

```python
matrix = [[1, 2], [3, 4], [5, 6]]

for row in matrix:
    for item in row:
        print(item)
```

**Output:**

```
1
2
3
4
5
6
```

## Key Points

- **`for item in list:`** - simple iteration over values
- **`range(len(list))`** - loop with index access
- **`enumerate(list)`** - get both index and value
- `enumerate()` returns **tuples** `(index, value)`
- **Unpack** enumerate tuples: `for index, value in enumerate(list)`
- `enumerate(list, start=n)` - custom starting index
- Use **index** when you need to modify items
- **`enumerate()`** is more Pythonic than `range(len())`
