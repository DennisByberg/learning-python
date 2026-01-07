# While Loops

## What are While Loops?

Execute code **repeatedly** as long as a condition is `True`.

```python
i = 1

while i <= 5:
    print(i)
    i += 1

# Output: 1, 2, 3, 4, 5
```

## While vs For Loops

- **For loops** - when you know the **number of iterations**
- **While loops** - when you don't know how many times to loop

## Practical Example - User Input

```python
command = ""

while command.lower() != "quit":
    command = input("> ")
    print("ECHO", command)

# Keeps running until user types "quit"
```

## Infinite Loops

**Be careful!** If the condition never becomes `False`, the loop runs forever.

```python
# Infinite loop - DON'T RUN THIS!
while True:
    print("This will run forever")
```

## Breaking Out of While Loops

Use `break` to exit early:

```python
while True:
    command = input("> ")
    if command.lower() == "quit":
        break
    print("ECHO", command)
```

## Common Pattern - Retry Logic

```python
attempts = 0

while attempts < 3:
    password = input("Password: ")
    if password == "secret":
        print("Access granted")
        break
    attempts += 1
    print(f"Wrong! {3 - attempts} attempts left")
else:
    print("Too many attempts")
```

## Key Points

- **While loops** run as long as condition is `True`
- Use when you **don't know** how many iterations needed
- **Infinite loops** occur if condition never becomes `False`
- Use **`break`** to exit early
- Can use **`else`** clause (executes if no `break`)
