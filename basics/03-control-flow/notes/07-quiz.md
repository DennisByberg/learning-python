# Quiz

## Question

What will we see on the terminal?

```python
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
```

**Answer: `c`**

**Explanation:**

1. `10 == "10"` → `False` (different types: int vs string)
2. `"bag" > "apple"` → `True` (b > a in Unicode)
3. `"bag" > "cat"` → `False` (b < c in Unicode)
4. `True and False` → `False`
5. All conditions are `False`, so `else` executes

## Key Concepts Tested

- **Type comparison** - Different types are not equal
- **String comparison** - Uses Unicode values
- **Logical operators** - `and` requires both to be `True`
- **Control flow** - `if-elif-else` execution order
