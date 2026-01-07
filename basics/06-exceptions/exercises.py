"""
EXERCISES - EXCEPTIONS
======================
Follow the instructions below. Comment out exercises you're not working on.
Run the program after each exercise to test your solution.
"""

# ============================================================================
# EXERCISE 1: Basic Try/Except
print("\n" + "=" * 60)
print("EXERCISE 1: Basic Try/Except")
print("=" * 60)
# ============================================================================
# Ask the user for their age (use input())
# Convert it to an integer
# If the user enters invalid input (e.g., "abc"), catch the ValueError
# Print "Invalid age" if error occurs, otherwise print "Valid age: <age>"
# Expected behavior:
# Input "25" -> "Valid age: 25"
# Input "abc" -> "Invalid age"


# YOUR CODE HERE:

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age!")
else:
    print(f"Your age is: {age}")


# ============================================================================
# EXERCISE 2: Multiple Exceptions
print("\n" + "=" * 60)
print("EXERCISE 2: Multiple Exceptions")
print("=" * 60)
# ============================================================================
# Create a list: numbers = [10, 20, 30]
# Ask user for an index (use input() and convert to int)
# Print the number at that index
# Handle both ValueError (invalid number) and IndexError (index out of range)
# Expected behavior:
# Input "1" -> 20
# Input "abc" -> "Please enter a valid number"
# Input "10" -> "Index out of range"


# YOUR CODE HERE:
numbers = [10, 20, 30]

try:
    user_index = int(input("Enter index: "))
    print(numbers[user_index])
except ValueError:
    print("Please enter a valid number")
except IndexError:
    print("Index out of range")

# ============================================================================
# EXERCISE 3: File Handling with Try/Except
print("\n" + "=" * 60)
print("EXERCISE 3: File Handling with Try/Except")
print("=" * 60)
# ============================================================================
# Try to open a file called "data.txt" for reading
# If the file doesn't exist, catch FileNotFoundError
# Print "File not found" if error occurs
# If file exists, print "File opened successfully"
# Expected behavior:
# If data.txt doesn't exist -> "File not found"
# If data.txt exists -> "File opened successfully"


# YOUR CODE HERE:
try:
    with open("data.txt") as file:
        print("File opened successfully")
except FileNotFoundError:
    print("File not found")


# ============================================================================
# EXERCISE 4: Using Finally
print("\n" + "=" * 60)
print("EXERCISE 4: Using Finally")
print("=" * 60)
# ============================================================================
# Try to divide 100 by a number from user input
# Handle ZeroDivisionError if user enters 0
# Use finally to print "Calculation attempt completed"
# Expected behavior:
# Input "5" -> 20.0, "Calculation attempt completed"
# Input "0" -> "Cannot divide by zero", "Calculation attempt completed"


# YOUR CODE HERE:
try:
    user_input = int(input("Divide 100 with: "))
    print(100 / user_input)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Calculation attempt completed")
