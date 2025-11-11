# Iterables

## What are Iterables?

An **iterable** is any object that can be looped over with a `for` loop.

```python
# Check type
print(type(5))           # <class 'int'>
print(type(range(5)))    # <class 'range'>
```

## Common Iterables

### Range

```python
for number in range(5):
    print(number)
# Output: 0, 1, 2, 3, 4
```

### Strings

```python
for char in "Python":
    print(char)
# Output: P, y, t, h, o, n
```

### Lists

```python
for name in ["Dennis", "Polka", "Sune"]:
    print(name)
# Output: Dennis, Polka, Sune
```

## Other Iterables

```python
# Tuples
for item in (1, 2, 3):
    print(item)

# Sets
for item in {1, 2, 3}:
    print(item)

# Dictionaries (iterates over keys)
for key in {"name": "John", "age": 25}:
    print(key)
```

## Key Points

- **Iterable** - any object you can loop over
- Common iterables: **range**, **strings**, **lists**, **tuples**, **sets**, **dictionaries**
- Use `for` loops to iterate over them
- Each iterable has its own type (`range`, `str`, `list`, etc.)
