import math

"""
EXERCISES - PRIMITIVE TYPES
============================
Follow the instructions below. Comment out exercises you're not working on.
Run the program after each exercise to test your solution.
"""

# ============================================================================
# EXERCISE 1: Variables & Variable Names
print("\n" + "=" * 60)
print("EXERCISE 1: Variables & Variable Names")
print("=" * 60)
# ============================================================================
# Create the following variables with descriptive names (snake_case):
# - A number of students (1500)
# - A course rating (4.85)
# - Whether the course is published (True)
# - A course name ("Python for Beginners")

# YOUR CODE HERE:
student_count = 1500
course_rating = 4.85
is_published = True
course_name = "Python for Beginners"

# Test (should print your variables):
print(f"Students: {student_count}")
print(f"Rating: {course_rating}")
print(f"Published: {is_published}")
print(f"Course: {course_name}")


# ============================================================================
# EXERCISE 2: Strings - Indexing & Slicing
print("\n" + "=" * 60)
print("EXERCISE 2: Strings - Indexing & Slicing")
print("=" * 60)
# ============================================================================
# Use this string:
text = "Python Programming"

# Write code that:
# a) Prints the first letter ("P")
# b) Prints the last letter ("g")
# c) Prints the first 6 letters ("Python")
# d) Prints the last 11 letters ("Programming")
# e) Prints the entire string backwards

# YOUR CODE HERE:
print(text[0])
print(text[-1])
print(text[0:6])
print(text[7:])
print(text[::-1])

# ============================================================================
# EXERCISE 3: Escape Sequences
print("\n" + "=" * 60)
print("EXERCISE 3: Escape Sequences")
print("=" * 60)
# ============================================================================
# Create variables that contain:
# a) A string with your name and age on separate lines (use \n)
# b) A Windows file path: C:\Users\Dennis\Documents
# c) A string that contains both single and double quotes:
#    He said "It's a beautiful day!"

# YOUR CODE HERE:
info_name = "John"
info_age = 25

info = f"{info_name}\n{info_age}"
file_path = "C:\\Users\\YourName\\Documents"
quote = 'He said "It\'s a beautiful day!"'

# Test:
print(info)
print(file_path)
print(quote)


# ============================================================================
# EXERCISE 4: Formatted Strings (F-strings)

# ============================================================================
# Create variables for your first name, last name, and age.
# Use an f-string to create an introduction:
# "Hello! My name is [first] [last] and I am [age] years old."

# YOUR CODE HERE:
firstname = "John"
lastname = "Doe"
age = 25

introduction = f"Hello! My name is {firstname} {lastname} and I am {age} years old."

# Test:
print("\n" + "=" * 60)
print("EXERCISE 4: Formatted Strings (F-strings)")
print("=" * 60)
print(introduction)


# ============================================================================
# EXERCISE 5: String Methods
print("\n" + "=" * 60)
print("EXERCISE 5: String Methods")
print("=" * 60)
# ============================================================================
# Use this string:
messy_text = "   python programming   "

# Write code that:
# a) Removes whitespace from both sides
# b) Makes all letters uppercase
# c) Makes the first letter of each word uppercase (title case)
# d) Finds the index of the word "programming"
# e) Replaces "python" with "Java"
# f) Checks if "pro" is in the string

# YOUR CODE HERE:

print(f"Messy text: {messy_text}")
print(messy_text.strip())
print(messy_text.strip().upper())
print(messy_text.strip().title())
print(messy_text.strip().index("programming"))
print(messy_text.strip().replace("python", "Java"))
print(messy_text.find("pro"))


# ============================================================================
# EXERCISE 6: Numbers - Basic Operations
print("\n" + "=" * 60)
print("EXERCISE 6: Numbers - Basic Operations")
print("=" * 60)
# ============================================================================
# Calculate the following:
# a) The sum of 47 and 89
# b) The product of 12 and 8
# c) 100 divided by 7 (float division)
# d) 100 divided by 7 (integer division)
# e) The remainder when 100 is divided by 7
# f) 2 to the power of 10

# YOUR CODE HERE:

print(f"The sum of 47 and 89: {47 + 89}")
print(f"The product of 12 and 8: {12 * 8}")
print(f"100 divided by 7 (float division): {100 / 7}")
print(f"100 divided by 7 (integer division): {100 // 7}")
print(f"The remainder when 100 is divided by 7: {100 % 7}")
print(f"2 to the power of 10: {2 ** 10}")


# ============================================================================
# EXERCISE 7: Augmented Assignment Operators
print("\n" + "=" * 60)
print("EXERCISE 7: Augmented Assignment Operators")
print("=" * 60)
# ============================================================================
# Start with:
x = 100
# Use augmented operators to:
# a) Add 50
# b) Multiply by 2
# c) Divide by 3
# d) Raise to the power of 2

# YOUR CODE HERE:
print(x + 50)
print(x * 2)
print(x / 3)
print(x**2)

# ============================================================================
# EXERCISE 8: Working with Numbers
print("\n" + "=" * 60)
print("EXERCISE 8: Working with Numbers")
print("=" * 60)
# ============================================================================
# Import the math module and:
# a) Round 5.7 up
# b) Round 5.7 down
# c) Calculate the square root of 144
# d) Calculate the absolute value of -25.5
# e) Print the value of pi

# YOUR CODE HERE:
print(math.ceil(5.7))
print(math.floor(5.7))
print(math.sqrt(144))
print(abs(-25.5))
print(math.pi)


# ============================================================================
# EXERCISE 9: Type Conversion
print("\n" + "=" * 60)
print("EXERCISE 9: Type Conversion")
print("=" * 60)
# ============================================================================
# a) Convert the string "42" to an integer
# b) Convert the integer 100 to a string
# c) Convert the string "3.14" to a float

# YOUR CODE HERE:
# a)
string_42 = "42"
int_32 = int(string_42)

print(type(string_42))  # <class 'str'>
print(type(int_32))  # <class 'int'>

# b)
integer_100 = 100
print(type(integer_100))  # <class 'int'>
print(type(str(integer_100)))  # <class 'str'>

# c)
string_314 = 314
print(type(string_314))  # <class 'int'>
print(type(float(string_314)))  # <class 'float'>


# ============================================================================
# FINAL EXERCISE: Mini-Calculator
print("\n" + "=" * 60)
print("FINAL EXERCISE: Mini-Calculator")
print("=" * 60)
# ============================================================================
# Create a simple mini-calculator that:
# 1. Asks the user for two numbers (use input and convert to float)
# 2. Calculates: sum, difference, product, division
# 3. Presents the results nicely with f-strings (2 decimals)
#
# Example output:
# Number 1: 10
# Number 2: 3
# ================
# 10.0 + 3.0 = 13.00
# 10.0 - 3.0 = 7.00
# 10.0 * 3.0 = 30.00
# 10.0 / 3.0 = 3.33

# YOUR CODE HERE
# input1 = input("Enter number 1: ")
# input2 = input("Enter number 2: ")

# num1 = float(input1)
# num2 = float(input2)


# print(f"Number 1: {num1}")
# print(f"Number 2: {num2}")
# print("================")
# print(f"{num1} + {num2} = {num1 + num2:.2f}")
# print(f"{num1} - {num2} = {num1 - num2:.2f}")
# print(f"{num1} * {num2} = {num1 * num2:.2f}")
# print(f"{num1} / {num2} = {num1 / num2:.2f}")


# ============================================================================
# BONUS CHALLENGE: Text Analyzer
print("\n" + "=" * 60)
print("BONUS CHALLENGE: Text Analyzer")
print("=" * 60)
# ============================================================================
# Create a program that:
# 1. Asks the user for a sentence
# 2. Displays:
#    - Number of characters (including spaces)
#    - Number of characters (without spaces)
#    - The sentence in uppercase
#    - The sentence in lowercase
#    - The sentence in reverse order
#    - Number of words (tip: use .split() and len())

# YOUR CODE HERE:
# sentence = input("Enter a sentence: ")
sentence = "Hello The World"
print(f"Number of characters (including spaces): {len(sentence)}")
print(f"Number of characters (without spaces): {len(sentence.replace(" ", ""))}")
print(f"The sentence in uppercase: {sentence.upper()}")
print(f"The sentence in lowercase: {sentence.lower()}")
print(f"The sentence in reverse order: {sentence[::-1]}")
print(f"Number of words: {len(sentence.split())}")
