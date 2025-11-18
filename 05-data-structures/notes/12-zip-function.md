# Zip Function

## What is Zip?

`zip()` combines multiple iterables (lists, tuples, strings) into tuples, pairing up elements at the same index.

## Syntax

```python
zip(iterable1, iterable2, ...)
```

## Basic Examples

```python
# Combine two lists
list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = list(zip(list1, list2))
print(result)  # [(1, 10), (2, 20), (3, 30)]

# Combine three iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
list3 = ["a", "b", "c"]
result = list(zip(list1, list2, list3))
print(result)  # [(1, 10, 'a'), (2, 20, 'b'), (3, 30, 'c')]

# Zip with strings
result = list(zip("abc", [1, 2, 3]))
print(result)  # [('a', 1), ('b', 2), ('c', 3)]
```

## Unequal Length Lists

```python
# Zip stops at the shortest iterable
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30]
result = list(zip(list1, list2))
print(result)  # [(1, 10), (2, 20), (3, 30)]
# Note: 4 and 5 are ignored
```

## Common Use Cases

```python
# Create a dictionary from two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "Stockholm"]
person = dict(zip(keys, values))
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'Stockholm'}

# Iterate over two lists simultaneously
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78
```

## Unzipping

```python
# Unzip using zip with *
pairs = [(1, 10), (2, 20), (3, 30)]
list1, list2 = zip(*pairs)
print(list1)  # (1, 2, 3)
print(list2)  # (10, 20, 30)
# Note: Returns tuples, not lists
```

## Zip with List Comprehension

```python
# Add corresponding elements
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = [x + y for x, y in zip(list1, list2)]
print(sums)  # [11, 22, 33]

# Combine strings
first_names = ["John", "Jane", "Bob"]
last_names = ["Doe", "Smith", "Johnson"]
full_names = [f"{first} {last}" for first, last in zip(first_names, last_names)]
print(full_names)  # ['John Doe', 'Jane Smith', 'Bob Johnson']
```

## Key Points

- `zip()` returns a zip object (use `list()` to convert)
- Combines elements at the same index from multiple iterables
- Stops at the shortest iterable
- Commonly used to create dictionaries
- Useful for parallel iteration
- Can be "unzipped" using `zip(*iterable)`

## When to Use Zip

- Combining related data from multiple lists
- Creating dictionaries from separate keys and values
- Iterating over multiple lists simultaneously
- Transposing data (rows to columns)
