# Getting Started with Python - Quiz

Test your knowledge of the Python basics covered in this section.

### Question 1: What does a linter do?

<details>
<summary>Click to reveal answer</summary>

A linter checks your code for errors and style issues. It analyzes your code without running it and helps identify:

- Syntax errors
- Style guide violations (like PEP 8)
- Potential bugs
- Code quality issues

Examples of Python linters include pylint, flake8, and the built-in linting in VS Code's Python extension.

</details>

### Question 2: What is a syntax error?

<details>
<summary>Click to reveal answer</summary>

A syntax error is a grammar mistake in your Python code that violates the language's rules. It prevents your code from running because Python cannot understand what you're trying to do.

Examples:

- Missing parentheses: `print "Hello"` (should be `print("Hello")`)
- Incomplete expressions: `2 >` (missing right side of comparison)
- Incorrect indentation
- Missing colons after if statements

When you get a syntax error, Python will show you where the error occurred and give you a hint about what's wrong.

</details>

### Question 3: What is an expression?

<details>
<summary>Click to reveal answer</summary>

An expression is a piece of code that produces or evaluates to a value. Expressions can be:

**Simple expressions:**

- `5` (a number)
- `"Hello"` (a string)
- `x` (a variable)

**Complex expressions:**

- `2 + 3` (arithmetic operation, evaluates to 5)
- `2 > 1` (comparison, evaluates to True)
- `"Hello" * 3` (string multiplication, evaluates to "HelloHelloHello")

The key point is that expressions always result in a value that can be used elsewhere in your code.

</details>

## Bonus Questions

### Question 4: What are the two main parts of Python?

<details>
<summary>Click to reveal answer</summary>

1. **Language (Rules)** - The syntax, grammar, and features that define how Python code should look and behave
2. **Implementation (Program)** - The actual software that reads and executes Python code (like CPython, Jython, PyPy)
</details>

### Question 5: What happens when you run a Python program?

<details>
<summary>Click to reveal answer</summary>

1. **Source Code** - Your `.py` file with human-readable Python code
2. **Compilation** - CPython compiles your code into Python Bytecode
3. **Execution** - Python Virtual Machine (PVM) executes the bytecode
4. **Machine Code** - PVM converts bytecode to machine instructions
5. **Output** - You see the results of your program

This two-step process (source → bytecode → machine code) makes Python platform-independent.

</details>

### Question 6: Why use Black formatter over autopep8?

<details>
<summary>Click to reveal answer</summary>

**Black** is generally preferred because:

- **Zero configuration** - Works out of the box
- **Consistent results** - Same formatting every time
- **Opinionated** - No debates about style choices
- **Modern adoption** - Used by major Python projects
- **Great VS Code integration**

**autopep8** is more conservative and configurable, but Black's "uncompromising" approach leads to more consistent code
