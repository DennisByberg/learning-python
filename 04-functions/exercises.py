"""
EXERCISES - FUNCTIONS
======================
Follow the instructions below. Comment out exercises you're not working on.
Run the program after each exercise to test your solution.
"""

# ============================================================================
# EXERCISE 1: Defining Functions
print("\n" + "=" * 60)
print("EXERCISE 1: Defining Functions")
print("=" * 60)
# ============================================================================
# Create a function called greet_user() that prints "Hello, User!"
# Call the function to test it.


# YOUR CODE HERE:
def greet_user():
    print("Hello, User!")


greet_user()

# ============================================================================
# EXERCISE 2: Arguments
print("\n" + "=" * 60)
print("EXERCISE 2: Arguments")
print("=" * 60)
# ============================================================================
# Create a function called greet_person(name) that prints "Hello, {name}!"
# Call it with your name.


# YOUR CODE HERE:
def greet_person(name):
    print(f"Hello {name}!")


greet_person("Dennis")

# ============================================================================
# EXERCISE 3: Return Values
print("\n" + "=" * 60)
print("EXERCISE 3: Return Values")
print("=" * 60)
# ============================================================================
# Create a function called square(number) that returns the square of a number
# Call it with the number 5 and print the result
# Expected output: 25


# YOUR CODE HERE:
def square(number):
    return number**2


print(square(5))


# ============================================================================
# EXERCISE 4: Multiple Parameters
print("\n" + "=" * 60)
print("EXERCISE 4: Multiple Parameters")
print("=" * 60)
# ============================================================================
# Create a function called add(a, b) that returns the sum of two numbers
# Call it with 10 and 20, print the result
# Expected output: 30


# YOUR CODE HERE:
def add(a, b):
    return a + b


print(add(10, 20))


# ============================================================================
# EXERCISE 5: Keyword Arguments
print("\n" + "=" * 60)
print("EXERCISE 5: Keyword Arguments")
print("=" * 60)
# ============================================================================
# Create a function called describe_person(name, age, city)
# that prints: "{name} is {age} years old and lives in {city}"
# Call it using keyword arguments in any order


# YOUR CODE HERE:
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")


describe_person(name="Dennis", age=31, city="Gothenburg")


# ============================================================================
# EXERCISE 6: Default Arguments
print("\n" + "=" * 60)
print("EXERCISE 6: Default Arguments")
print("=" * 60)
# ============================================================================
# Create a function called power(base, exponent=2) that returns base^exponent
# Call it with just one argument (should square the number)
# Call it with two arguments
# Expected outputs:
# power(3) -> 9
# power(2, 3) -> 8


# YOUR CODE HERE:
def power(base, exponent=2):
    return base**exponent


print(power(3))
print(power(2, 3))


# ============================================================================
# EXERCISE 7: xargs (*args)
print("\n" + "=" * 60)
print("EXERCISE 7: xargs (*args)")
print("=" * 60)
# ============================================================================
# Create a function called sum_all(*numbers) that returns the sum of all numbers
# Test it with different amounts of arguments:
# sum_all(1, 2, 3) -> 6
# sum_all(10, 20, 30, 40) -> 100


# YOUR CODE HERE:
def sum_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40))

# ============================================================================
# EXERCISE 8: xxargs (**kwargs)
print("\n" + "=" * 60)
print("EXERCISE 8: xxargs (**kwargs)")
print("=" * 60)
# ============================================================================
# Create a function called save_user(**user) that prints all key-value pairs
# Call it with: save_user(id=1, name="Alice", age=25, city="Stockholm")
# Expected output format:
# id: 1
# name: Alice
# age: 25
# city: Stockholm


# YOUR CODE HERE:
def save_user(**user):
    for key, value in user.items():
        print(f"{key}: {value}")


save_user(id=1, name="Alice", age=25, city="Stockholm")


# ============================================================================
# EXERCISE 9: Combining Parameters
print("\n" + "=" * 60)
print("EXERCISE 9: Combining Parameters")
print("=" * 60)
# ============================================================================
# Create a function: create_user(username, *hobbies, **details)
# That prints:
# - Username: {username}
# - Hobbies: {hobbies tuple}
# - Details: {details dict}
# Call it: create_user("alice123", "reading", "gaming", age=25, city="Stockholm")


# YOUR CODE HERE:
def create_user(username, *hobbies, **details):
    print(f"Username: {username}")
    print(f"Hobbies: {hobbies}")
    print(f"Details: {details}")


create_user("alice123", "reading", "gaming", age=25, city="Stockholm")

# ============================================================================
# EXERCISE 10: FizzBuzz
print("\n" + "=" * 60)
print("EXERCISE 10: FizzBuzz")
print("=" * 60)
# ============================================================================
# Create a function called fizzbuzz(n) that prints numbers from 1 to n
# Rules:
# - If number is divisible by 3: print "Fizz"
# - If number is divisible by 5: print "Buzz"
# - If divisible by both 3 and 5: print "FizzBuzz"
# - Otherwise: print the number
# Call fizzbuzz(15)
# Expected output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz


# YOUR CODE HERE:
def fizzbuzz(n):
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


fizzbuzz(15)


# ============================================================================
# EXERCISE 11: Temperature Converter
print("\n" + "=" * 60)
print("EXERCISE 11: Temperature Converter")
print("=" * 60)
# ============================================================================
# Create a function called convert_temperature(temp, unit="C")
# - If unit is "C", convert Celsius to Fahrenheit: (C * 9/5) + 32
# - If unit is "F", convert Fahrenheit to Celsius: (F - 32) * 5/9
# - Return the converted value
# Test:
# convert_temperature(0) -> 32.0 (0°C to °F)
# convert_temperature(32, "F") -> 0.0 (32°F to °C)


# YOUR CODE HERE:
def convert_temperature(temp, unit="C"):
    if unit == "C":
        return (temp * 9 / 5) + 32
    elif unit == "F":
        return (temp - 32) * 5 / 9


print(f"{convert_temperature(0)}°F")
print(f"{convert_temperature(32, "F")}°C")
