# Python Interpreter

## What is the Python Interpreter?

The Python interpreter is an interactive environment where you can write and execute Python code line by line. It's useful for testing small pieces of code, performing calculations, and learning Python syntax.

## Starting the Interpreter

```bash
python
# or
python3
```

This opens the interactive Python shell where you can type Python commands.

## Basic Examples

### Simple Arithmetic

```python
>>> 2 + 2
4
```

### Boolean Comparisons

```python
>>> 2 > 1
True

>>> 2 > 5
False
```

### Syntax Errors

When you write invalid Python syntax, the interpreter shows an error:

```python
>>> 2 >
  File "<stdin>", line 1
    2 >
       ^
SyntaxError: invalid syntax
```

This is a **syntax error** - it means there's a grammar mistake in the code. In this case, the comparison operator `>` expects something to compare with on the right side.

## Key Points

- The interpreter executes code immediately when you press Enter
- `>>>` is the primary prompt where you type commands
- Syntax errors show you exactly where the grammar mistake occurred
- The interpreter is great for testing small snippets and learning Python

## Exiting the Interpreter

```python
>>> exit()
# or
>>> quit()
# or press Ctrl+D (Linux/Mac) or Ctrl+
```
