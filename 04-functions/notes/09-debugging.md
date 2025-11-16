# Debugging

## What is Debugging?

Debugging is the process of **finding and fixing errors** in your code.

## Using the Debugger in VS Code

Instead of using `print()` statements everywhere, use VS Code's **debugger**.

### Setting Breakpoints

1. Click in the **left margin** next to a line number
2. A **red dot** appears - this is a breakpoint
3. Code execution will **pause** at this line

```python
def multiply(*numbers):
    total = 1
    for number in numbers:  # Set breakpoint here
        total *= number
    return total

print("Start")
print(multiply(1, 2, 3))
```

### Starting the Debugger

1. Press **F5** or click **Run → Start Debugging**
2. Select **Python File**
3. Code runs until it hits a breakpoint

### Debugger Controls

- **F10** (Step Over) - Execute current line, move to next
- **F11** (Step Into) - Go inside function calls
- **Shift + F11** (Step Out) - Exit current function
- **F5** (Continue) - Run until next breakpoint
- **Shift + F5** (Stop) - Stop debugging

### Inspecting Variables

When paused at a breakpoint, you can:

- **Hover** over variables to see their values
- Check the **Variables** panel on the left
- Use the **Debug Console** to evaluate expressions

### Debug Console

Type expressions in the Debug Console while paused:

```python
total        # Check value of total
number * 2   # Evaluate expressions
type(numbers) # Check variable types
```

## Why Use a Debugger?

**Print Statements (Bad):**

```python
def calculate(a, b):
    print(f"a: {a}")  # Clutters code
    print(f"b: {b}")
    result = a + b
    print(f"result: {result}")
    return result
```

**Debugger (Good):**

- Set breakpoint
- Inspect all variables at once
- Step through code line by line
- No code changes needed

## Key Points

- **Debugging** finds and fixes errors in code
- Use **breakpoints** instead of print statements
- Click left margin to set a **red dot** breakpoint
- **F5** starts debugging
- **F10** steps over, **F11** steps into
- Inspect variables in the **Variables panel**
- Use **Debug Console** to evaluate expressions
- Clean, professional way to understand code flow
