"""
EXERCISES - CONTROL FLOW
=========================
Follow the instructions below. Comment out exercises you're not working on.
Run the program after each exercise to test your solution.
"""

# ============================================================================
# EXERCISE 1: Even Numbers
print("\n" + "=" * 60)
print("EXERCISE 1: Even Numbers")
print("=" * 60)
# ============================================================================
# Write a program that displays the even numbers between 1 and 10.
# Example output:
# 2
# 4
# 6
# 8
# We have 4 even numbers

# YOUR CODE HERE:
even_numbers_count = 0

for num in range(1, 10):
    if num % 2 == 0:
        print(num)
        even_numbers_count += 1
print(f"We have {even_numbers_count} even numbers")


# ============================================================================
# EXERCISE 2: Comparison Operators
print("\n" + "=" * 60)
print("EXERCISE 2: Comparison Operators")
print("=" * 60)
# ============================================================================
# Create a variable age = 20
# Write code that checks:
# a) Is age greater than or equal to 18?
# b) Is age less than 65?
# c) Is age equal to 20?
# d) Is age not equal to 25?
# Print the result of each comparison

# YOUR CODE HERE:
driver_age = 20

print(driver_age >= 18)
print(driver_age < 65)
print(driver_age == 20)
print(driver_age != 25)


# ============================================================================
# EXERCISE 3: If-Elif-Else
print("\n" + "=" * 60)
print("EXERCISE 3: If-Elif-Else")
print("=" * 60)
# ============================================================================
# Create a variable score = 75
# Write an if-elif-else statement that prints:
# - "Excellent" if score >= 90
# - "Good" if score >= 70
# - "Pass" if score >= 50
# - "Fail" if score < 50

# YOUR CODE HERE:
student_score = 91
if student_score >= 90:
    comment = "Excellent"
elif student_score >= 70:
    comment = "Good"
elif student_score >= 50:
    comment = "Pass"
else:
    comment = "Fail"
print(comment)


# ============================================================================
# EXERCISE 4: Ternary Operator
print("\n" + "=" * 60)
print("EXERCISE 4: Ternary Operator")
print("=" * 60)
# ============================================================================
# Create a variable temperature = 22
# Use a ternary operator to set a variable weather to:
# - "Hot" if temperature > 25
# - "Cold" otherwise
# Print the weather variable

# YOUR CODE HERE:
temperature = 26

print("Hot" if temperature > 25 else "Cold")


# ============================================================================
# EXERCISE 5: Logical Operators
print("\n" + "=" * 60)
print("EXERCISE 5: Logical Operators")
print("=" * 60)
# ============================================================================
# Create variables:
# has_license = True
# age = 20
#
# Write an if statement that checks if someone can drive:
# They can drive if they have a license AND are 18 or older
# Print "Can drive" or "Cannot drive"

# YOUR CODE HERE:
has_license = True
age = 17

print("Can drive" if (has_license and age >= 18) else "Cannot drive")


# ============================================================================
# EXERCISE 6: Chaining Comparison Operators
print("\n" + "=" * 60)
print("EXERCISE 6: Chaining Comparison Operators")
print("=" * 60)
# ============================================================================
# Create a variable price = 50
# Use chaining to check if price is between 10 and 100 (inclusive)
# Print "Valid price" or "Invalid price"

# YOUR CODE HERE:
price = 9
print("Valid price" if 10 <= price <= 100 else "Invalid price")


# ============================================================================
# EXERCISE 7: For Loop - Sum
print("\n" + "=" * 60)
print("EXERCISE 7: For Loop - Sum")
print("=" * 60)
# ============================================================================
# Write a for loop that calculates the sum of numbers from 1 to 10
# Print the final sum
# Expected output: 55

# YOUR CODE HERE:
total_sum = 0
for num in range(1, 11):
    total_sum += num
print(total_sum)


# ============================================================================
# EXERCISE 8: For Loop - Multiplication Table
print("\n" + "=" * 60)
print("EXERCISE 8: For Loop - Multiplication Table")
print("=" * 60)
# ============================================================================
# Write a program that prints the multiplication table for 5
# Output should be:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50

# YOUR CODE HERE:
multiplier = 5
for num in range(1, 11):
    print(f"{multiplier} x {num} = {multiplier * num}")


# ============================================================================
# EXERCISE 9: For-Else
print("\n" + "=" * 60)
print("EXERCISE 9: For-Else")
print("=" * 60)
# ============================================================================
# Create a list: numbers = [1, 3, 5, 7, 9]
# Write a for loop that searches for the number 4
# If found, print "Found!" and break
# If not found (else clause), print "Not found!"

# YOUR CODE HERE:
numbers = [1, 3, 5, 7, 9]
number_to_find = 4
for num in numbers:
    if num == number_to_find:
        print("Found!")
        break
else:
    print("Not Found!")


# ============================================================================
# EXERCISE 10: Nested Loops - Rectangle
print("\n" + "=" * 60)
print("EXERCISE 10: Nested Loops - Rectangle")
print("=" * 60)
# ============================================================================
# Use nested loops to print a 4x5 rectangle of asterisks
# Expected output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# YOUR CODE HERE:
for row in range(4):
    for col in range(5):
        print("*", end=" ")
    print()


# ============================================================================
# EXERCISE 11: While Loop - Countdown
print("\n" + "=" * 60)
print("EXERCISE 11: While Loop - Countdown")
print("=" * 60)
# ============================================================================
# Write a while loop that counts down from 5 to 1
# Then print "Blast off!"
# Expected output:
# 5
# 4
# 3
# 2
# 1
# Blast off!

# YOUR CODE HERE:
countdown = 5
while countdown != 0:
    print(countdown)
    countdown -= 1
print("Blast off!")


print("\n✅ Exercises complete! Run the program to test your solutions.")
