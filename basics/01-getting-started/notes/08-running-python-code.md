# Running Python Code

## Different Ways to Run Python Code

There are several ways to execute your Python programs, each with its own advantages.

## 1. Using the Terminal

The most basic way to run Python code is through the terminal:

```bash
# Navigate to your file location
cd 01-getting-started/exercises

# Run the Python file
python app.py
# or
python3 app.py
```

## 2. VS Code Play Button

VS Code provides a convenient play button (▶️) in the top-right corner when you have a Python file open. Simply click it to run your code.

## 3. Right-click Menu

Right-click anywhere in your Python file and select "Run Python File in Terminal" from the context menu.

## 4. Command Palette

Press `Ctrl+Shift+P` to open the command palette, then type "Python: Run Python File in Terminal" and press Enter.

## 5. Custom Keyboard Shortcut (My Setup)

I've configured a custom keyboard shortcut for faster code execution:

**Shortcut:** `Ctrl+R`

### Setting up the shortcut:

1. Press `Ctrl+Shift+P` to open Command Palette
2. Type "Preferences: Open Keyboard Shortcuts"
3. Search for "Python: Run Python File in Terminal"
4. Click the pencil icon and set your preferred shortcut
5. I use `Ctrl+R` for quick execution

## Benefits of Using Shortcuts

- **Faster workflow** - No need to reach for the mouse
- **Keeps hands on keyboard** - More efficient coding
- **Quick testing** - Instantly run code while developing

## Running Code Output

When you run Python code, the output appears in VS Code's integrated terminal at the bottom of the screen. You can see:

- Print statements
- Error messages
- Program results

## Example

```python
# app.py
print("Hello World!")
x = 1
print(x)
```

**Output:**

```
Hello World!
1
```

## Tips

- Use `Ctrl+R` (or your custom shortcut) for quick execution
- The integrated terminal shows both your code output and any errors
- You can have multiple terminal sessions open for different tasks
